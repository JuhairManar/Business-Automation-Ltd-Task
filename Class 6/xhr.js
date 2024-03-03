document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the button and the div elements
    let buttonFour = document.getElementById('one');
    let divFour = document.getElementsByTagName('div')[0];

    // Add a click event listener to the button
    buttonFour.addEventListener('click', () => {
        console.log("hi");
        // Step 1: create our ajax object
        let xhr = new XMLHttpRequest();
        
        // Step 2: configure our request
        xhr.open("GET", "https://icanhazdadjoke.com");
        xhr.setRequestHeader('Accept', "application/json");
        
        // Step 3: define our callback function
        xhr.onreadystatechange = function() {
            // 4 = XHR request is completed
            if (xhr.readyState === 4 && xhr.status === 200) {
                const jsonData = JSON.parse(xhr.responseText);
                // Update the text content of the div with the joke
                divFour.innerText = jsonData.joke;
            }
        };

        // Step 4: send the request
        xhr.send();
    });
});

