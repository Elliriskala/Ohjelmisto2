'use strict';

console.log(window);
// BOM - browser object model
// window.alert('moi');
// alert('moi');

/**
// confirm palauttaa boolean arvon (true/false)
if (confirm('Vahvistatko?')) {
  console.log('käyttäjä klikkasi OK.')
} else {
  console.log('käyttäjä painoi peruuta.')
}

// promp palauttaa käyttäjän syöttäjän merkkijonon, jos painetaan ok
// palauttaa null, jos painetaan calcel
const userInput = prompt('Sano jotain: ');
console.log('user input', userInput);

*/

// DOM - document object model
console.log(window.document);

const targetElements = document.querySelector('p');
console.log(targetElements);

// id aina yksilöllinen
const targetElement = document.querySelector('#toka');
console.log(targetElement);

targetElement.textContent = 'tässä JS:n kautta muokattu sisältö';

// HTML-elementtien luominen ja lisääminen DOMiin
const newParagraph = document.createElement('p');

document.querySelector('article').append(newParagraph);
newParagraph.textContent = 'Tässä uusi teksti sisältö.'
newParagraph.innerHTML = 'Tässä <b>uusi</b> teksti sisältö.'
// newParagraph.style = 'color: blue';
newParagraph.classList.add('blue');

// viittaus kaikkiin p-elementteihin löytyy targetElements-muuttujasta
// käsitellään ensimmäistä niistä
targetElements.classList.add('bold');

// tapahtuman käsittely (event-olio sisältää tietoa tapahtumasta)
function clickHandler(event) {
  console.log('p clicked', event);
}

// klikkien käsittely
targetElements.addEventListener('click', clickHandler);

// kaksoisklikin (context menu) käsittely koko dokumentille (nimentön funktio)
document.addEventListener('contextmenu', function(event){
  console.log('context menu', event);
  event.preventDefault();
});

// key logger
const keyPressHistory = [];
document.addEventListener('keyup', function (event){
  console.log('näppäin ylös', event.key);
  keyPressHistory.push(event.key);
  console.log('näppäin painallus historia', keyPressHistory.toString());
});

// hiirenseuranta
document.addEventListener('mousemove', function (event){
  console.log('mouse position', event.clientX, event.clientY);
});