'use strict';

// ASSIGNMENT 3.
// Write a program that prompts for three integers.
// The program prints the sum, product and average of the numbers to the HTML document. (3p)
// remember to convert strings to numbers when adding

const sum = document.querySelector('.sum');
const product = document.querySelector('.product');
const average = document.querySelector('.average');

const num1 = parseInt(prompt('Please give an integer: '));
const num2 = parseInt(prompt('Please give an integer: '));
const num3 = parseInt(prompt('Please give an integer: '));

let totalSum = num1 + num2 + num3;
let totalProduct = num1 * num2 * num3;
let totalAverage = totalProduct / 3;

sum.innerHTML = `Sum: ${totalSum}`;
product.innerHTML = `Product: ${totalProduct}`;
average.innerHTML = `Average: ${totalAverage}`;