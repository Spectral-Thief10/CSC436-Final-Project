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
import random

load_dotenv()

APP_ID = "797268582819317"
APP_SECRET = os.getenv("APP_SECRET")
REDIRECT_URI = "http://localhost:8000/callback"

user_access_token = "EAALVHI6rZAfUBRD9R3gMy1i5pYuiuXasf3yygjYTi1ITYEGdvgmbUVRTlM6tfOdhLLySO81EBZAo9AAzZCA6rgsZAPZBxcXBkUxvi0oM24Ds1ZC0efHsZAu4F7Hf5agV9ufkrtq0TssKrqg9B8IJLlZBZAEEpvYhl0vcAw7ygPpKHws6wPn8SZAiVZAAqiBhWsu"
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
    if (image==""):
        return facebookPOST.txt(user_access_token,text, facebook_page_id)
    else:
        return facebookPOST.img(user_access_token,text,image, facebook_page_id)

@eel.expose
def postToInstagram(text):
    image_url = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Test_file_by_Davod.png" 

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

@eel.expose
def writeLoginFile(facebookUsername,facebookPassword,instagramUsername,instagramPassword):
    with open("login.json", "w") as f:
        x = {"facebook": {"username":facebookUsername, "password":facebookPassword},
             "instagram":{"username":instagramUsername, "password":instagramPassword}}
        
        f.write(json.dumps(x))

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

@eel.expose()
def getRandomReview():
    messages = GetReviews.GetText()
    i = random.randint(0, len(messages) - 1)
    message = messages[i]
    eel.changeText(message)

# Start the index.html file
eel.start("index.html")
