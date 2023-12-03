'use strict';

// ASSIGNMENT 5
// Make an app that retrieves a random Chuck Norris joke and displays it
// in the console. (2p)
// API to use: chucknorris.io
// Send a request to https://api.chucknorris.io/jokes/random and
// print only the joke to the console (that would be the 'value' property)
// No need to add a form.

// ASSIGNMENT 6
// Develop the app further (4p).
// Now add a form where you can enter a search term like in assignments 1-3
// Send the search term to
// https://api.chucknorris.io/jokes/search?query=${value_from_input}
// using fetch()
// Print each joke in this format:
// <article>
//     <p>Joke here<p>
// </article>

async function getJoke() {
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const joke = await response.json();
    console.log('Joke:', joke.value);
  } catch (error) {
    console.log('fetch error', error);
  }
}

getJoke();


// ASSIGNMENT 6

/**
document.querySelector('#search').addEventListener('click', async function (event) {
  event.preventDefault();

  const search = document.querySelector('#search');

  let jokeContent;
  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${search}`);
    const joke = await response.json();
    console.log('Joke:', joke);
    jokeContent = joke.value;

    const article = document.createElement('article');
    const content = document.createElement('p');
    content.textContent = jokeContent;
    article.appendChild(content);
    document.querySelector('#jokeHere').appendChild(article);

  } catch (error) {
    console.log('fetch error', error);
    jokeContent = 'Ei vitsiä saatavilla';
  }
});

*/
