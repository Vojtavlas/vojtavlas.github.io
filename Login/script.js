function validateLogin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    // Simple validation (you can replace this with your own authentication logic)
    if (username === "user" && password === "password") {
        // Successful login
        errorMessage.innerHTML = "";

        // Redirect to the specified URL
        window.location.href = "https://vojtavlas.github.io/Aes";
    } else {
        // Failed login
        errorMessage.innerHTML = "Invalid username or password";
    }
}
