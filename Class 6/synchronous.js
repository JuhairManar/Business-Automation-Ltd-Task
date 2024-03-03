let buttonThree = document.getElementById('three');
let divThree = document.getElementsByTagName('div')[0];

buttonThree.addEventListener('click', displayJoke);

function displayJoke() {
    console.log("hi");
    
    fetch("https://icanhazdadjoke.com", {
        headers: { "Accept": "application/json" }
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(jokeObject) {
        const lowercaseJoke = jokeObject.joke.toLowerCase();
        divThree.innerHTML = lowercaseJoke;
    })
    .catch(function(error) {
        console.error('Error fetching joke:', error);
    });
}

