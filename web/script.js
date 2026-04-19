

function post(){
    facebook = document.getElementById("Facebook").checked
    instagram = document.getElementById("Instagram").checked
    text = document.getElementById("Text").value
    image = document.getElementById("image").value; 
    
    facebookPageId = document.getElementById("getPageID").value; 

    if(facebook){
        eel.postToFacebook(text,image,facebookPageId)
    }
    if(instagram){
        eel.postToInstagram(text,image)
    }
}

function loginInstagram() {
  // The app's ID.
  const clientId = "797268582819317";
  // Send user back to RSMS app.
  const redirectUri = "http://localhost:8000/callback";
  // Required permissions for Instagram API
  const scope = "pages_show_list,pages_read_engagement,instagram_basic,instagram_content_publish,business_management";
  // Redirects user to log into meta, once done, sends user back to RSMS.
  window.open(`https://www.facebook.com/v19.0/dialog/oauth?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scope}&response_type=code`);
}

function getRandomReview(){
    eel.getRandomReview()
}

function selectImage(){
    eel.selectImage();
}

eel.expose(changeText)
function changeText(text){

    document.getElementById("Text").innerHTML = text
}

eel.expose(changeImagePath)
function changeImagePath(imagePath){
    document.getElementById("image").value = imagePath
}

eel.expose(printError)
function printError(message){
    window.alert(message)
}

function notification(){
    dateTime = document.getElementById("dateTime").value
    window.alert(dateTime)
}

// Onclick of the buttons
document.querySelector("button").onclick = post
document.getElementById("imageButton").onclick = selectImage
document.getElementById("reviewButton").onclick = getRandomReview
document.getElementById("notificationButton").onclick = notification
function schedulePost() {
    const text = document.getElementById("Text").value;
    const day = document.getElementById("scheduleDay").value;
    const time = document.getElementById("scheduleTime").value;
    const repeat = document.getElementById("repeatType").value;

    if (!time) {
        alert("Please select a time");
        return;
    }

    const [hour, minute] = time.split(":").map(Number);

    eel.createCalendarEvent(
        "Social Media Post Reminder",
        text,
        day,
        hour,
        minute,
        repeat
    )
}

// Onclick of the button
document.querySelector("button").onclick = post
