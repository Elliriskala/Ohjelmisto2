'use strict';

// ASSIGNMENT 7
// Open t7 folder in your IDE/editor. Make a hover effect with JavaScript.(2p)
// when user mouses over <p id="trigger"> change
// the picture of <img id="target"> form picA.jpg to picB.jpg
// when user mouses off, change the picture back to original

const moveMouse = document.querySelector('#trigger');

const targetElement = document.querySelector('#target');
const firstPic = 'img/picA.jpg';
const secondPic = 'img/picB.jpg';

moveMouse.addEventListener('mouseover', function (event) {
  targetElement.src = secondPic;
});

moveMouse.addEventListener('mouseout', function (event) {
  targetElement.src = firstPic;
});
