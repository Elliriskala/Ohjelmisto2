'use strict';

// ASSIGNMENT 2.
// Write a program that prompts for user's name and then greets the user.
// Print the result to the HTML document: Hello, Name!

// haetaan html elementti
const fillName = document.querySelector('#fillName');

// pyydetään nimi
const name = prompt('Please give your name: ');
console.log(name);

// printataan h2 elementti
fillName.innerHTML = `Hello ${name}!`;

// voi tehdä myös näin:
// document.querySelector('#fillName').innerHTML = `Hello ${name}!`;