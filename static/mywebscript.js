const API_URL = 'http://localhost:8080';

async function translateToFrench() {
    textToTranslate = document.getElementById("textToTranslate").value;
    const data = await getData({route: 'englishToFrench', textToTranslate});
    document.querySelector("#translated_text").innerHTML = data[0].translation;
}


async function translateToEnglish() {
    textToTranslate = document.getElementById("textToTranslate").value;
    const data = await getData({route: 'frenchToEnglish', textToTranslate});
    document.querySelector("#translated_text").innerHTML = data[0].translation;
}
async function translateToSpanish() {
    textToTranslate = document.getElementById("textToTranslate").value;
    const data = await getData({route: 'englishToSpanish', textToTranslate});
    document.querySelector("#translated_text").innerHTML = data[0].translation;  
}
function getData({route, textToTranslate})
{
    return new Promise((resolve, reject) => {
        window.fetch(`${API_URL}/${route}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                textToTranslate
            })
        })
        .then((res) => res.json())
        .then(resolve)
        .catch(reject)
    })
}
// let translateToFrench = ()=>{
//     textToTranslate = document.getElementById("textToTranslate").value;

//     let xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             document.getElementById("translated_text").innerHTML = xhttp.responseText;
//         }
//     };
//     xhttp.open("GET", "englishToFrench?textToTranslate"+"="+textToTranslate, true);
//     xhttp.send();
// }

// let translateToEnglish = ()=>{
//     textToTranslate = document.getElementById("textToTranslate").value;

//     let xhttp = new XMLHttpRequest();
//     xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//             document.getElementById("translated_text").innerHTML = xhttp.responseText;
//         }
//     };
//     xhttp.open("GET", "frenchToEnglish?textToTranslate"+"="+textToTranslate, true);
//     xhttp.send();
// }
