'use script';

// ASSIGNMENT 6
// Open t6 folder in your IDE/editor. Make a script that opens an
// alert window that says 'Button Clicked' when the <button> element
// is clicked. (1p)

const clickButton = document.querySelector('button');

function clickHandler(event) {
  alert('Button Clicked');
}

clickButton.addEventListener('click', clickHandler);

