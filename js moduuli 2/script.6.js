'use strict';

// ASSIGNMENT 6
// Write a function that returns a random dice roll between 1 and 6.
// The function should not have any parameters. Write a main program
// that rolls the dice until the result is 6. The main program should
// print out the result of each roll in an unordered list (<ul>). (2p)

let diceRolled = document.querySelector('#dice');
function diceRoll() {
  let result = Math.floor(Math.random() * 6 + 1);
  return result;
}

let game = false;
while (!game) {
  let dice = diceRoll()
  if (dice === 6) {
    game = true;
      console.log(`You threw ${dice}.`);
      break;
  } else console.log(dice);
}

