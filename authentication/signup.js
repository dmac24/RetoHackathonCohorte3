import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/10.7.2/firebase-auth.js"

const firebaseConfig = {
    apiKey: "AIzaSyDeCJGzb78lBIKBNKLngsJhOaXDU6l9qyM",
    authDomain: "uphoney-ef208.firebaseapp.com",
    projectId: "uphoney-ef208",
    storageBucket: "uphoney-ef208.appspot.com",
    messagingSenderId: "242696645644",
    appId: "1:242696645644:web:9d67641a6556e475501229"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth();


const submit = document.getElementById('submit');
submit.addEventListener("click", function(event) {
    event.preventDefault()
    //inputs
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    createUserWithEmailAndPassword(auth, email, password)
    .then((userCredential) => {
        // Signed up 
        const user = userCredential.user;
        alert("Creando Cuenta...")
        window.location.href = "../index.html";
        // ...
    })
    .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        alert("Se necesita usuario y contraseña")
        // ..
    });
})


