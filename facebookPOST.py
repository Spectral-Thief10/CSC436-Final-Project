"""
filename: facebookPOST.py
author: Joshua S. Andrews
purpose: to post a message to a facebook feed utilizing facebook-sdk
"""
import facebook

graph = facebook.GraphAPI("access_token=token")

if len(sys.argv) == 1:
	graph.put_photo(image=open(image_path, 'rb'), message)
else if len(sys.argv) == 2:
	graph.put_object(parent_object='me', connection_name='feed', message)
else:
    print('Got to posting without a post?')


if __name__ == "__main__":
    '''
    sys.args
        1 = access_token
        2 = message
        3 = image_path
    '''
    if len(sys.argv) < 2:
        token= sys.argv[1]
        message = sys.argv[2] 
        if len(sys.argv) == 3:
            image_path = sys.argv[3]
    else
        print("Needs [Token, Message, <image>] to POST to facebook")