'use strict';

// ASSIGNMENT 2
// Write a program that asks the user for the number of participants.
// After this, the program asks for the names of all participants.
// Finally, the program prints the names of the participants on the
// web page in an ordered list (<ol>) in alphabetical order. (2p)

const participant = parseInt(prompt('How many participants are there?'))

const participants = [];
for(let i=1; i<=participant; i++) {
  const name = prompt('What is the name of the '+ i + '. participant?');
  participants.push(name);
}

console.log(participants);

