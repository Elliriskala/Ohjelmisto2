'use strict';

// ASSIGNMENT 1
// Write a program that prompts the user for five numbers and prints them in
// the reverse order they were entered. Print the result to the console.(2p)
// Save the numbers to an array, then use for-loop to iterate in reverse order.
// Do not use array.reverse() function.

const numbers = [];
for (let i=0; i<5; i++) {
  const number = parseInt(prompt('Please enter a number'));
  numbers.push(number);
}

console.log('Your numbers in reverse order:')

for (let num=numbers.length - 1; num>=0; num --) {
  console.log(numbers[num]);
}

