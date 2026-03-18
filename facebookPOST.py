"""
filename: facebookPOST.py
author: Joshua S. Andrews
purpose: to post a message to a facebook feed utilizing facebook-sdk
"""
import facebook

def img(token, message, image_path):
    graph = facebook.GraphAPI("access_token="+token)
	graph.put_photo(image=open(image_path, 'rb'), message)
def txt(token, msg):
    graph = facebook.GraphAPI("access_token="+token)
	graph.put_object(parent_object='me', connection_name='feed', message)

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
    else if length==3:
        img(sys.argv[1],sys.argv[2],sys.argv[3])
    else
        print("Needs [Token, Message, <image>] to POST to facebook")
