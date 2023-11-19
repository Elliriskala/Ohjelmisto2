'use strict';

// ASSIGNMENT 4
// Write a program that asks the user for numbers until he gives zero.
// The given numbers are printed in the console from the largest
// to the smallest. (2p)

const numbers = []
let untilZero = false;
while (!untilZero) {
  const number = parseInt(prompt('Please enter a number. If you enter zero the program will end.'));
  if (number === 0) {
    untilZero = true;
      break
  } else {
    numbers.push(number);
  }
}

console.log(numbers.sort((a, b) => b - a));


