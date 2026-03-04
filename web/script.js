

function post(){
    facebook = document.getElementById("Facebook").checked
    instagram = document.getElementById("Instagram").checked
    text = document.getElementById("Text").value
    if(facebook){
        eel.postToFacebook(text)
    }
    if(instagram){
        eel.postToInstagram(text)
    }
}

// Onclick of the button
document.querySelector("button").onclick = post