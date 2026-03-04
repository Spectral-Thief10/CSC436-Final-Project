import eel

eel.init("web")  

@eel.expose
def postToFacebook(text):
    print(f"Posted: {text} to facebook")



@eel.expose
def postToInstagram(text):
    print(f"Posted: {text} to instagram")


# Start the index.html file
eel.start("index.html")