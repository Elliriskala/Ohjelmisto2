'use strict';

// ASSIGNMENT 7.
// Modify the function above so that it gets the number of sides on
// the dice as a parameter. With the modified function you can for
// example roll a 21-sided role-playing dice. The difference to
// the last exercise is that the dice rolling in the main program
// continues until the program gets the maximum number on the dice,
// which is asked from the user at the beginning. (2p)

let diceRolled = document.querySelector('#dice7');
const maxValue = parseInt(prompt('How many sides is on the dice?'));

function diceRoll(sides) {
  let result = Math.floor(Math.random() * maxValue + 1);
  return result;
}

let game = false;
while (!game) {
  let dice = diceRoll()
  if (dice === maxValue) {
    game = true;
      console.log(`You threw ${maxValue}.`);
      break;
  } else console.log(dice);
}