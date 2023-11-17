'use strict';

// ASSIGNMENT 8.
  // Write a program that prompts the user for the start and end year.
  // The program prints all leap years from the interval given by the user.
  // Printing is done in an unordered list to the HTML document. (3p)

const target = document.querySelector('#output');
const startYear = parseInt(prompt('Alkuvuosi?'));
const endYear = parseInt(prompt('Loppuvuosi?'));

const ul = document.createElement('ul');
target.append(ul);

for (let i=startYear; i<=endYear; i++) {
  if ((i % 4 == 0) && (i % 100 != 0) || (i % 400 == 0)) {
  const newLi = document.createElement('li');
  newLi.innerText = `The year ${i} is a leap year.`;
  ul.append(newLi);
  }
}

ul.style = 'list-style: none;'