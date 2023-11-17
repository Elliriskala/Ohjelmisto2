'use strict';

// ASSIGNMENT 7
// Write a program that rolls user defined number of dice and displays the sum
// of the results of the dice rolls.(2p)
// First, program asks the user for the number of dice rolls.
// Then the program throws a die as many times as the user defined.
// Print the sum of the results in the console or in the HTML document.

let game = document.querySelector('#diceGame');
let dice = parseInt(prompt('How many dice would you like to throw?'));

let diceTotal = 0;
let throws = 0;
while (throws != dice) {
  const numDice = Math.floor(Math.random() * 6 + 1);
  diceTotal = diceTotal + numDice;
  console.log(numDice);
  throws++;
  if (throws == dice) {
    game.innerHTML = `You threw ${dice} dice, the sum of the thrown dice is: ${diceTotal}`;
  }
}
