function validateLogin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    // Fetch user data from a JSON file (replace with your JSON file path)
    fetch('users.json')
        .then(response => response.json())
        .then(users => {
            // Simulated authentication (replace with your authentication logic)
            const user = users.find(u => u.username === username && u.password === password);

            if (user) {
                // Successful login
                errorMessage.innerHTML = "";
                alert("Login successful! Redirect to your desired page.");
            } else {
                // Failed login
                errorMessage.innerHTML = "Invalid username or password";
            }
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
            errorMessage.innerHTML = "Error fetching user data";
        });
}
