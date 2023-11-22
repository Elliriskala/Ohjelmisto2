'use strict';

// Open t2 folder in your IDE/editor. Add HTML by using createElement()
// and appendChild methods. (2p)
// Add the following HTML code to the element with id="target"
// <li>First item</li>
// <li>Second item</li>
// <li>Third item</li>
// Add class my-item to the second list item

const listItems = document.querySelector('#target');

listItems.innerHTML = "";
let listItem1 = document.createElement("li");
    listItem1.textContent = 'First item';
let listItem2 = document.createElement("li");
    listItem2.textContent = 'Second item'
    listItem2.classList.add('my-item');
let listItem3 = document.createElement("li");
    listItem3.textContent = 'Third item';

listItems.appendChild(listItem1);
listItems.appendChild(listItem2);
listItems.appendChild(listItem3);


