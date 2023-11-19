'use strict';

// ASSIGNMENT 5
// Write a program that prompts the user for numbers.
// When the user enters one of the numbers he previously entered,
// the program will announce that the number has already been given
// and stops its operation and then prints all the given numbers to
// the console in ascending order. (2p)

const numbers = [];
let alreadyGivenNumber = false;
while (!alreadyGivenNumber) {
  const number = parseInt(prompt('Please enter a number:'));
  if (numbers.includes(number)) {
    alreadyGivenNumber = true;
  } else numbers.push(number);
}

let giveNumber = document.querySelector('#alreadyGiven');
giveNumber.innerHTML = `You have already gave this number.`
console.log(numbers.sort((a, b) => a-b));