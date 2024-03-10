console.log("Hello from JS")

const uri = "http:/localhost:6969/api"
const ask = {
    method: 'get',
    headers: {
        "Content-Type": "application/json; charset=utf-8"
    },
    mode: "cors",
}

function GetData() {
    fetch("http://localhost:6969/api").then((response) => {
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`)
        }
        return response.text();
    }).then((text) => {
        console.log(text)

        el = document.getElementById("servedData")
        el.innerText = text.split(" ")[1]
    })
}
