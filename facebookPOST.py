"""
filename: facebookPOST.py
author: Joshua S. Andrews
purpose: to post a message to a facebook feed utilizing facebook-sdk
"""

def img(token, message, image_path,facebook_page_id):
    import requests
    
    page_id=getFacebook_page_id(facebook_page_id)
    
    post_url= f'https://graph.facebook.com/{page_id}/feed'
    
    params = {
        'access_token': token
    }
    data = {
        'message': msg
    }
    files = {
        'source': open(image_path, 'rb')
    }
    

    try:
        response = requests.post(url=post_url, params=params, data=data, files=files)
        
        if response.status_code == 200:
            post_id = response.json().get('id')
            print(f"Successfully posted: Post ID: {post_id}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def txt(token, msg,facebook_page_id):
    import requests
    
    page_id=getFacebook_page_id(facebook_page_id)
    
    post_url= f'https://graph.facebook.com/{page_id}/feed'
    
    payload = { 'message': msg,
                'access_token': token
    }
    
    try:
        response = requests.post(post_url, data=payload)
        
        if response.status_code == 200:
            post_id = response.json().get('id')
            print(f"Successfully posted: Post ID: {post_id}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def getFacebook_page_id(facebook_page_id):
    ''' 
    Check if facebook_page_id.txt exists, if not have user enter page ID 
    and create file, then return text from file
    '''
    if (facebook_page_id is ""):
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
            f.close
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
    if length==4:
        if (sys.argv[3] is ""):
            txt(sys.argv[1],sys.argv[2], sys.argv[4])
        else:
            img(sys.argv[1],sys.argv[2],sys.argv[3], sys.argv[4])
    else:
        print("Needs [Token, Message, <image_path>, facebook_page_id] to POST to facebook")
