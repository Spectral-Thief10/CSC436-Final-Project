import eel
import requests
from dotenv import load_dotenv
from bottle import route, request
import time
import os
import json
import facebookPOST
import schedulePosts
import GetReviews
import GetTestimonials
import random
import time
import requests
import cloudinary
import cloudinary.uploader
import tkinter 
import tkinter.filedialog as filedialog

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

APP_ID = "797268582819317"
APP_SECRET = os.getenv("APP_SECRET")
REDIRECT_URI = "http://localhost:8000/callback"

def uploadToCloudinary(file_path):
    try:
        response = cloudinary.uploader.upload(file_path)
        return {
            "url": response["secure_url"],
            "public_id": response["public_id"]
        }
    except Exception as e:
        print("Cloudinary upload error:", e)
        return None

def deleteFromCloudinary(public_id):
    try:
        result = cloudinary.uploader.destroy(public_id)
        print("Deleted from Cloudinary:", result)
    except Exception as e:
        print("Error deleting image:", e)

user_access_token = None
user_instagram_id = None

# This function runs right as Meta sends the user back to RSMS.
@route('/callback')
def callback():
    # Get necessary tokens to access user account
    global user_access_token
    global user_instagram_id

    # Get code/proof user logged in successfully
    code = request.query.code

    print("Authorization code:", code)

    # use the login code to turn into an access token.
    short_token = changeCodeForToken(code)
    # change the short-lived access token of about an hour to a long-lived one of mutliple days.
    long_token = makeTokenLong(short_token)

    user_access_token = long_token

    print("User access token is:", long_token)

    # use access token to get instagram id.
    user_instagram_id = getInstagramBusinessID(user_access_token)

    return "<h2>Instagram login was successful. You can close this window.</h2>"

eel.init("web")  

@eel.expose
def postToFacebook(text,image, facebook_page_id):
    print("going to facebookPost.py")
    token = facebookPOST.get_token()
    print(f"token: {token}")
    facebook_page_id = facebookPOST.getFacebook_page_id(facebook_page_id)
    if image == "":
        return facebookPOST.txt(token, text, facebook_page_id)
    else:
        return facebookPOST.img(token,text,image, facebook_page_id)

@eel.expose
def postToInstagram(text, image):

    if(user_access_token == None):
        eel.printError("Post falied. Please login to Instagram")
        return
    
    file_path = resolveImagePath(image)

    if file_path is None:
        print("No image provided")
        return
    
    upload = uploadToCloudinary(file_path)

    if upload is None:
        print("failed to upload image")
        return
    
    image_url = upload["url"]
    public_id = upload["public_id"]
    
    print("Public Image URL:", image_url)

    # create a media container
    create_url = f"https://graph.facebook.com/v19.0/{user_instagram_id}/media"
    payload = {
        "image_url": image_url,
        "caption": text,
        "access_token": user_access_token
    }

    create_response = requests.post(create_url, data=payload)
    create_data = create_response.json()

    if "id" not in create_data:
        print("Error creating media:", create_data)
        return
    
    container_id = create_data["id"]

    # wait for the media to be ready
    status_url = f"https://graph.facebook.com/v19.0/{container_id}"

    # wait up to 10 seconds
    for i in range(10): 
        status_response = requests.get(status_url, params={
            "fields": "status_code",
            "access_token": user_access_token
        }).json()

        status = status_response.get("status_code")
        print("Status:", status)

        if status == "FINISHED":
            break

        time.sleep(1)

    # publish to instagram
    publish_url = f"https://graph.facebook.com/v19.0/{user_instagram_id}/media_publish"
    publish_payload = {
        "creation_id": container_id,
        "access_token": user_access_token
    }

    publish_response = requests.post(publish_url, data=publish_payload)
    publish_data = publish_response.json()

    print("Instagram response:", publish_data)

    print(f"Posted: {text} to Instagram")

    deleteFromCloudinary(public_id)

def changeCodeForToken(code):
    url = "https://graph.facebook.com/v19.0/oauth/access_token"
    params = {
        "client_id": APP_ID,
        "redirect_uri": REDIRECT_URI,
        "client_secret": APP_SECRET,
        "code": code
    }
    response = requests.get(url, params=params).json()
    return response["access_token"]

def makeTokenLong(short_token):
    url = "https://graph.facebook.com/v19.0/oauth/access_token"
    params = {
        "grant_type": "fb_exchange_token",
        "client_id": APP_ID,
        "client_secret": APP_SECRET,
        "fb_exchange_token": short_token
    }
    response = requests.get(url, params=params).json()
    return response["access_token"]

def getInstagramBusinessID(access_token):

    # get all the pages that the user manages
    pages_url = "https://graph.facebook.com/v19.0/me/accounts"
    pages_params = {
        "access_token": access_token
    }

    pages_response = requests.get(pages_url, params=pages_params).json()

    # if could not find pages
    if "data" not in pages_response or len(pages_response["data"]) == 0:
        print("No pages found:", pages_response)
        return None

    # loop through each page to find connected instagram account
    for page in pages_response["data"]:
        page_id = page["id"]
        print("Checking page:", page_id)

        # check if page has an instagram account
        ig_url = f"https://graph.facebook.com/v19.0/{page_id}"
        ig_params = {
            "fields": "instagram_business_account",
            "access_token": access_token
        }

        ig_response = requests.get(ig_url, params=ig_params).json()

        # if yes, then return the instagram business id
        if "instagram_business_account" in ig_response:
            ig_id = ig_response["instagram_business_account"]["id"]
            print("Found Instagram Business ID:", ig_id)
            return ig_id

    # else, return no account found
    print("No Instagram business account found on any page.")
    return None

def resolveImagePath(image_input):
    if not image_input:
        return None

    # If user already gave full path
    if os.path.exists(image_input):
        return image_input

    # If user gave just filename, assume it's in /web
    web_path = os.path.join("web", image_input)

    if os.path.exists(web_path):
        return web_path

    print("Image not found:", image_input)
    return None

@eel.expose()
def getRandomReview():
    reviews = GetReviews.GetText()
    tesimonials = GetTestimonials.GetTestimonials()
    messages = reviews + tesimonials
    i = random.randint(0, len(messages) - 1)
    message = messages[i]
    print(message)
    eel.changeText(message)

@eel.expose
def selectImage():
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
    )
    print(image_path)
    eel.changeImagePath(image_path)


# Start the index.html file
eel.start("index.html")
