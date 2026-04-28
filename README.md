# CSC436-Final-Project README

Expected Behavior
1. Application launches and opens browser
2. If program has not been run, requests logins for social media sites (index.html)
3. Goes to Input Page (main.html)
4. User selects which site(s) to post to and enters <text> and <PathToImg> then clicks submit
  OR
   User schedules desired reminders and clicks submit
5. Confirmation message on success or failure of operation is rendered

To Get Business Page ID for posting to facebook
1. Log into https://business.facebook.com/
2. Click on settings on side pane
3. Click on Page Name
4. Page ID is listed under Page Info

#### DUE TO NOT CONTINUING SUPPORT POST PRODUCTION ###
To use app for posting to facebook
1. Have internal IT personnel register as Meta Developer
2. Create a user token through the Facebook Graph API browser site for app
3. Replace line # 93 of facebookPOST.py with:
     return "YOUR_USER_ACCESS_TOKEN"
4. Delete the token.txt file
5. Add business facebook page to App's Facebook Graph API with the following permissions:
     1. pages_read_engagement
     2. public_profile
     3. pages_manage_posts
     4. pages_manage_engagement
     5. pages_show_list
     6. business_management
  6. Register and publish app through Facebook Graph API browser UI
