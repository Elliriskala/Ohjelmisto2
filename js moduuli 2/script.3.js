'use strict';

// ASSIGNMENT 3.
// Write a program that asks for the names of six dogs.
// The program prints dog names to unordered list <ul> in reverse
// alphabetical order. (2p)

function getDogNames() {
  const dogs = [];
  for (let i=0; i<6; i++) {
    const dogName = prompt('What is the name of the dog?')
    dogs.push(dogName)
  }
  return dogs;
}

function dogNamesInOrder(dogs) {
  dogs.sort().reverse();
  let dogList = document.querySelector('#dognames');
  dogList.innerHTML = "";
  dogs.forEach(function (name) {
    let li = document.createElement("li");
    li.textContent = name;
    dogList.appendChild(li);
  });
}

let yourDogs= getDogNames();
dogNamesInOrder(yourDogs);



