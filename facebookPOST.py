# """
# filename: facebookPOST.py
# author: Joshua S. Andrews
# purpose: to post a message to a facebook feed utilizing facebook-sdk
# """
# import facebook

# def img(token, message, image_path):
#     graph = facebook.GraphAPI(access_token=token)
#     try:
#         graph.put_photo(image=open(image_path, 'rb'), message=message)
#     except:
#         print(f"Error posting img to facebook: {e}")

# def txt(token, msg):
#     graph = facebook.GraphAPI(access_token=token)
#     try:
#         graph.put_object(parent_object='me', connection_name='feed', message=msg)
#     except:
#         print(f"Error posting txt to facebook: {e}")
        
# if __name__ == "__main__":
#     import sys
#     '''
#     sys.args
#         1 = access_token
#         2 = message
#         3 = image_path
#     '''
#     length=len(sys.argv)
#     if length==2:
#         txt(sys.argv[1],sys.argv[2])
#     elif length==3:
#         img(sys.argv[1],sys.argv[2],sys.argv[3])
#     else:
#         print("Needs [Token, Message, <image>] to POST to facebook")
