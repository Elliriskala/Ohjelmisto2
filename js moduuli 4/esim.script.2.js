'use strict';

async function getMultiply(num) {
  try {
    const response = await fetch('http://127.0.0.1:3000/multiply/' + num);
    const json = await response.json();
    console.log('result:', json.result);
    return json;
  } catch (error) {
    console.error('getMultiply fetch fail', error);
  }
}

// asynkronkista funktiota pitää kutsua await-sanalla, jos haluaa sen
// palauttavan jotain mutta kuin promise olion
async function doMultiply () {
  // const num = prompt('Anna numero:');
  const num = document.querySelector('input').value;
  const resultJson = await getMultiply(num);
  const outputElement = document.querySelector('#toka');
  if (resultJson.result) {
    outputElement.textContent = 'tulos: ' + resultJson.result;
  } else {
    outputElement.textContent = `${resultJson.msg} (${resultJson.input_number})`;
  }
}

// sido DOMin ainoaan button-elementtiin tapahtumankäsittelijä
document.querySelector('button').addEventListener('click',
    function () {
      doMultiply();
});
