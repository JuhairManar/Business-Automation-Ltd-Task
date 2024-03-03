$(document).ready(function() {
    let jquery_button = $('#one');
    let jquery_div = $('div').eq(0);

    jquery_button.on('click', () => {
        console.log("hi");
        $.ajax({
            url: 'https://icanhazdadjoke.com',
            headers: { "Accept": "application/json" },
            success: (jokeObject) => {
                // Convert the joke to uppercase
                console.log(jokeObject);
                console.log(jokeObject.joke.toUpperCase());
                const joke = jokeObject.joke.toUpperCase();
                jquery_div.text(joke);
            },
            error: (xhr, status, error) => {
                // Handle errors 
                console.log('Sorry, there was an error:', error);
            }
        });
    });
});

