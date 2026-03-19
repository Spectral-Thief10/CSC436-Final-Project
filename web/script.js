

function post(){
    facebook = document.getElementById("Facebook").checked
    instagram = document.getElementById("Instagram").checked
    text = document.getElementById("Text").value
    image = document.getElementById("image").value; 
    
    if(facebook){
        eel.postToFacebook(text,image)
    }
    if(instagram){
        eel.postToInstagram(text,image)
    }
}

// Onclick of the button
document.querySelector("button").onclick = post