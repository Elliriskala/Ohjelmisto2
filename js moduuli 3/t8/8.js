'use strict';

// ASSIGNMENT 8
// Open t8 folder in your IDE/editor. Make a simple calculator. (4p)
// There are two input fields where user enters numbers.
// Based on the drop-down list, calculator performs addition,
// subtraction, multiplication or division of these two numbers.
// Use the value attribute of <option> elements to decide which
// operation the calculator needs to do. Example.
// Show the result in <p id="result"> when the button is clicked.

const form = document.querySelector('form');

const useCalculator = document.querySelector('#start');
useCalculator.addEventListener('click', calculate);

function calculate () {
  const num1 = parseInt(document.querySelector('#num1').value);
  const num2 = parseInt(document.querySelector('#num2').value);
  const calculator = document.querySelector('#operation').value;
  let result;
      if (calculator === 'add') {
        result = num1 + num2;
      } else if (calculator === 'sub') {
        result = num1 - num2;
      } else if (calculator === 'multi') {
        result = num1 * num2;
      } else if (calculator === 'div') {
        result = num1/num2;
      }
      document.querySelector('#result').innerHTML = 'Result: ' + result;
}





