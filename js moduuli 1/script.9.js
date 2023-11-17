'use strict';

// ASSIGNMENT 9
// Write a program that asks the user for an integer and tells if the number
// is a prime number. (2p) Prime numbers are numbers that are only divisible
// by 1 and itself. For example, number 13 is a prime number as it can only
// be divided by 1 or 13 so that the result is an integer.
// On the other hand, number 21 for example is not a prime number as it
// can be also be divided by numbers 3 and 7. Print the result on the HTML document.

let result = document.querySelector('#isPrime');
const num = parseInt(prompt('Insert a number'));


function primeNum(num) {
  if (num <= 1) return false;
  const primes = [2, 3, 5, 7];
  if (primes.includes(num)) return true;
  for (const x of primes) {
    if (num % x === 0) return false;
  }
  return true;
}

if (primeNum(num)) result.innerHTML = `Number ${num} is a prime number.`;
else result.innerHTML = `Number ${num} is not a prime number.`;





