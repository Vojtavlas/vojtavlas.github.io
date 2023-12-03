document.addEventListener('DOMContentLoaded', function () {
    // Get the button and counter elements
    var clickButton = document.getElementById('clickButton');
    var counterElement = document.getElementById('counter');

    // Initialize counter
    var counter = getCookie('counter') || 0;

    // Log the initial counter value
    console.log('Initial counter value:', counter);

    // Update the counter element with the initial value
    counterElement.textContent = counter;

    // Add click event listener to the button
    clickButton.addEventListener('click', function () {
        // Increment the counter
        counter++;

        // Update the counter element
        counterElement.textContent = counter;

        // Log the updated counter value
        console.log('Updated counter value:', counter);

        // Store the counter value in a cookie
        setCookie('counter', counter, 365);
    });

    // Function to set a cookie
    function setCookie(name, value, days) {
        var expires = '';
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = '; expires=' + date.toUTCString();
        }
        document.cookie = name + '=' + value + expires + '; path=/';

        // Log the set cookie
        console.log('Set cookie:', name, '=', value);
    }

    // Function to get a cookie value by name
    function getCookie(name) {
        var nameEQ = name + '=';
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    }
});
