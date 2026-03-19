function login() {

   facebookUsername = document.getElementById("FacebookUserName").value
   facebookPassword= document.getElementById("FacebookPassword").value


   instagramUsername = document.getElementById("InstagramUserName").value
   instagramPassword = document.getElementById("InstagramPassword").value

   eel.writeLoginFile(facebookUsername,facebookPassword,instagramUsername,instagramPassword)
   
   window.location.replace('main.html')
}

document.querySelector("button").onclick = login