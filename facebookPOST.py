"""
filename: facebookPOST.py
author: Joshua S. Andrews
purpose: to post a message to a facebook feed utilizing facebook-sdk
"""
import facebook

def img(token, message, image_path):
    graph = facebook.GraphAPI(access_token=token)
    try:
        graph.put_photo(image=open(image_path, 'rb'), message)
    except:
        print(f"Error posting img to facebook: {e}")

def txt(token, msg):
    import requests
    
    page_id=getFacebook_page_id(token)
    post_url= f'https://graph.facebook.com/{page_id}/feed
    
    payload = { 'message': msg,
                'access_token': token
    }
    
    try:
        response = requests.post(post_url, data=payload)
        response.raise_for_status()
        
        post_id = response.json().get('id')
        print(f"Successfully posted: Post ID: {post_id}")

def getFacebook_page_id(token):
    ''' 
    Retrieve facebook ID page associated with provided token
    '''
    url=f'https://graph.facebook.com/{token}'
    response=requests.get(url)
    data=response.json()
    
    page_id = data.get("id")
    return page_id
    
if __name__ == "__main__":
    import sys
    '''
    sys.args
        1 = access_token
        2 = message
        3 = image_path
    '''
    length=len(sys.argv)
    if length==2:
        txt(sys.argv[1],sys.argv[2])
    elif length==3:
        img(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print("Needs [Token, Message, <image>] to POST to facebook")
