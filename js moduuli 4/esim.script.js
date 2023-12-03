'use strict';

let coordinates;
// navigator.geolocation - selaimen tarjoama paikannusrajapinta
// takaisinkutsu (callback) - funktiot
function positionSuccess(position) {
  console.log('paikannus onnistui')
  coordinates = position.coords;
  console.log('sijaintikoordinaatit', coordinates.latitude, coordinates.longitude);
}

function positionError(error) {
  console.log('paikannus epäonnistui', error.message);
  // kerro käyttäjälle tässä, että homma meni pieleen
}

// starts the location search
navigator.geolocation.getCurrentPosition(
    positionSuccess,
    positionError,
    {enableHighAccuracy: true}
);

// huom asynkronisuus, koordinaatit eivät ole käytössä ennen kuin paikannettu
console.log('tulostuu geolocation-kutsun jälkeen', coordinates);

// Avoimet rajapinnat - Fetch ja AJAX

// moderni tapa, async await
async function getJoke() {
  let jokeContent;
  try {
    const response = await fetch('https://api.chucknorris.io/jokes/random');
    const joke = await response.json();
    console.log('joke:', joke)
    jokeContent = joke.value;
  } catch (error) {
    console.log('fetch error', error);
    jokeContent = 'Ei vitsiä saatavilla.';
  }
  document.querySelector('#toka').textContent = jokeContent;
}

getJoke();