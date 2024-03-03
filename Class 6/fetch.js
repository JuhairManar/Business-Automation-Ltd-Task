let buttonTwo = document.getElementById('two');
let divTwo = document.getElementsByTagName('div')[0];

buttonTwo.addEventListener('click', () => {
    console.log("hi");
    fetch('https://icanhazdadjoke.com', {
        headers: { "Accept": "application/json" }
    })
    .then((response) => {
        // Return the parsed JSON response
        return response.json();
    })
    .then((jokeObject) => {
        // Convert the joke to uppercase
        console.log('jokeObject', jokeObject);
        const joke = jokeObject.joke.toUpperCase();
        // Insert the result into the div element
        divTwo.innerText = joke;
    })
    .catch((error) => {
        // Handle any errors that occurred during the fetch
        console.log('Oh no, there was an error:', error);
    });
});

