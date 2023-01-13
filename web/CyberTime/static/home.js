function convert_timestamp() {
    let timestamp = document.getElementById('timestamp').value;
    let date = new Date(timestamp * 1000);
    document.getElementById('result').innerText = date.toUTCString();
}

let input = document.getElementById("feedback");
input.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
            let feedback = 'message=' + btoa(input.value);
            const xhttp = new XMLHttpRequest();
            xhttp.open("POST", "/feedback", false);
            xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xhttp.send(feedback);
            document.getElementById("admin_message").innerText = xhttp.responseText;
        }
    }
);