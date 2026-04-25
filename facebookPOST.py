"""
filename: facebookPOST.py
author: Joshua S. Andrews
purpose: to post a message to a facebook feed utilizing facebook-sdk
"""

def img(access_token, msg, image_path, page_id):
    print("Posting Image")
    import facebook
    graph = facebook.GraphAPI(access_token=access_token)
    
    with open(image_path, 'rb') as image:
        graph.put_photo(parent_object=page_id, connection_name='feed',image=image, message=msg)

def txt(access_token, msg, page_id):
    import facebook
    graph = facebook.GraphAPI(access_token=access_token)
    graph.put_object(parent_object=page_id, connection_name='feed', message=msg)

def get_token():
    """Gets a long-lived page access token from graph api"""
    import requests
    pages = get_page_access_token()
    page_access_token = pages['data'][0]['access_token']
    app_id = '1760179784929581'
    app_secret = '0e3a54441382b1b40fd1ccb6c08197de'
    graph_ver = "v25.0"

    url = f"https://graph.facebook.com/{graph_ver}/oauth/access_token"
    params = {
        'grant_type': 'fb_exchange_token',
        'client_id': app_id,
        'client_secret': app_secret,
        'fb_exchange_token': page_access_token
    }
    response = requests.get(url, params=params)
    return response.json().get('access_token')

def get_page_access_token():
    """Gets a short-lived page access token from graph API for
        all managed pages
    """
    import requests
    user_token = get_user_token()
    graph_ver = 'v25.0'

    url = f"https://graph.facebook.com/{graph_ver}/me/accounts"
    params = {
        'access_token': user_token
    }
    response = requests.get(url, params=params)
    data = response.json()

    if 'data' in data:
        for page in data['data']:
            print(f"Page Name: {page['name']}")
            print(f"Page ID: {page['id']}")
            print(f"Page Access Token: {page['access_token']}")
            print("-"*30)
    else:
        print("Error or no pages found:", data)
    return data

def get_user_token():
    """Gets a long-lived user token for app from graphAPI"""
    try:
        with open('token.txt', 'r') as f:
            print("token.txt exists!")
    except FileNotFoundError:
        import facebook
        token=get_short_user_token()
        graph = facebook.GraphAPI(access_token=token)
        app_id = '1760179784929581'
        app_secret = '0e3a54441382b1b40fd1ccb6c08197de'
        long_token= graph.extend_access_token(app_id=app_id, app_secret=app_secret)
        print(long_token)
        with open('token.txt', 'w') as f:
            f.write(str(long_token['access_token']))
            f.close()
        return long_token
    except IOError:
        print("File [token.txt] exists but is not accessible.")
    with open('token.txt', 'r') as f:
        contents = f.read()
        f.close()
        return contents

def get_short_user_token():
    """
    Returns manually entered short-lived token from browser based
    Graph API Explorer as a string
    """
    return "EAAZAA38rSUS0BRWG4tncTzOzJEOeUDwExU15G2XQUZCLjBDL7v9XZAlp0fIQ7maFZCXSZA9slO5giuWyfc0Y0XWAhZAZCugE34xJBMaTb4vwW5OeXEItqQO4ZBURZAtmvUHN4o5N8q2SNUqKB1vDG1ZCFZA2UjdbiARzcfzBQchqAcdP4fpXKqDzGlXzkWvZAjZA5qzp5M1ZA8ZAuFCtdSChVWygEApw3khPUAL5VbotkR2xI3ZB358uJUSRA0yKHMJ21fEGjpZCPa8BZBhP8bJZA32JuHaZB7RZCDgZDZD"


def getFacebook_page_id(facebook_page_id):
    '''
    Check if facebook_page_id.txt exists, if not have user enter page ID
    and create file, then return text from file
    '''
    if (facebook_page_id == ""):
        try:
            with open('facebook_page_id.txt', 'r') as f:
                contents=f.read()
                print("Page ID: " + contents)
                return contents
        except FileNotFoundError:
            print("To get page ID, log in to facebook and ")
            print("click about->page transparency->scroll to bottom for ID number")
            contents=input("Enter Page ID: ")
            with open('facebook_page_id.txt', 'w') as f:
                f.write(contents)
                f.close()
            return contents
    else:
        with open('facebook_page_id.txt', 'w') as f:
            f.write(facebook_page_id)
            f.close()
        return facebook_page_id
    
if __name__ == "__main__":
    import sys
    '''
    sys.args
        1 = access_token
        2 = message
        3 = image_path
        4 = facebook_page_id
    '''
    length=len(sys.argv)
    if length==5:
        if (sys.argv[3] == ""):
            print(txt(sys.argv[1],sys.argv[2], sys.argv[4]))
        else:
            print(img(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4]))
    else:
        print("Needs [Token, Message, image_path, facebook_page_id] to POST to facebook")
