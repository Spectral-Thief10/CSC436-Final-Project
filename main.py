import eel
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

eel.init("web")  

# To be changed so that it's the users' business id, this is just for testing rn
INSTAGRAM_BUSINESS_ID = "17841446410260449"
# same with the access token
ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")
print("Token loaded?:", bool(ACCESS_TOKEN))

@eel.expose
def postToFacebook(text,image):
    print(f"Posted: {text} to facebook")


# temporary, still need to make it so it works with anybody's instagram business account.
@eel.expose
def postToInstagram(text,image):
    image_url = "https://upload.wikimedia.org/wikipedia/commons/9/9f/Test_file_by_Davod.png" 

    create_url = f"https://graph.facebook.com/v19.0/{INSTAGRAM_BUSINESS_ID}/media"
    payload = {
        "image_url": image_url,
        "caption": text,
        "access_token": ACCESS_TOKEN
    }

    create_response = requests.post(create_url, data=payload)
    create_data = create_response.json()

    if "id" not in create_data:
        print("Error creating media:", create_data)
        return
    
    container_id = create_data["id"]

    publish_url = f"https://graph.facebook.com/v19.0/{INSTAGRAM_BUSINESS_ID}/media_publish"
    publish_payload = {
        "creation_id": container_id,
        "access_token": ACCESS_TOKEN
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

# Start the index.html file
eel.start("index.html")