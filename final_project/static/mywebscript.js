let translateToFrench = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "/englishToFrench?text=" + encodeURIComponent(textToTranslate), true); // Use "/englishToFrench" as the endpoint URL and pass the text as a query parameter
    xhttp.send();
}

let translateToEnglish = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "/frenchToEnglish?text=" + encodeURIComponent(textToTranslate), true); // Use "/frenchToEnglish" as the endpoint URL and pass the text as a query parameter
    xhttp.send();
}
