const video = document.getElementById("video");
const statusText = document.getElementById("status");

let currentToken = null;

// Start webcam immediately
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        statusText.innerText = "Camera access denied.";
    });

async function startChallenge() {
    statusText.innerText = "Requesting challenge...";

    const response = await fetch("http://127.0.0.1:5000/challenge");
    const data = await response.json();

    statusText.innerText = "Challenge: " + data.challenge.join(" → ");

    // Simulated verification request
    const verify = await fetch("http://127.0.0.1:5000/verify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nonce: data.nonce })
    });

    const result = await verify.json();

    if (result.success) {
        currentToken = result.token;
        statusText.innerText = "Proof of Life Verified ✅";
    } else {
        statusText.innerText = "Verification Failed ❌";
    }
}

async function accessProtected() {
    if (!currentToken) {
        statusText.innerText = "No valid Proof of Life token.";
        return;
    }

    const response = await fetch("http://127.0.0.1:5000/protected", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ token: currentToken })
    });

    const data = await response.json();
    statusText.innerText = data.message;
}
