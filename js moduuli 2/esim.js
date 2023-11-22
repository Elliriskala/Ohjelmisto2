'use strict';

// alkioiden tietotyypit voi olla mitä vaan
const items = ['eka', 2, 3.3, [1, 2, 3]];
console.log(items);

// alkion arvo saadaan alkion indeksiin viittaamalla
console.log(items[3]);

// alkion arvo voidaan lisätä muuttaa alkion indeksiin viittaamalla
items[3] = 99;
console.log(items[3])
items[9] = '10. alkion esimerkkiarvo';
console.log(items);

// arrayn koko
console.log(items.length);

console.log('Tulostetaan kaikkien alkioiden arvot For-silmukalla')
for (let i=0; i<=items.length; i++) {
  console.log(i+1 + '. alkion arvo on ' + items[i]);
}

// sama for of, ei tulosteta tyhjiä alkioita

for (const item of items) {
  if (item) { // undefined on epätoduudellinen (falsy)
    console.log(item);
  }
}

const names = ['jaakko', 'heikki', 'kalle', 'ville', 'aino', 'veeti'];
const ages = [13, 8, 20, 4, 6, 7];
console.log(names);
// järjestä aakkosjärjestykseen
names.sort();
console.log(names);
ages.sort((a, b) => b-a);
console.log(ages);
// käännä järjestys ympäri
ages.reverse();
console.log(ages);
// lisää uusi nimi loppuun
names.push('iines');
console.log(names);
// lisää uusi nimi taulukon alkuun
names.unshift('hessu');
console.log(names)

// names.pop() poistaa ja palauttaa viimeisen alkion
const lastNameInArr = names.pop();
console.log('taulukosta poistettiin', lastNameInArr);

// onko taulukossa arvo, palauttaa true/false boolean
console.log(names.includes('veeti'));

// JS objektit/oliot, olioliteraali on tietorakenteena kuin Pythonin sanakirja

const person = {
  name: 'iines',
  age: 34
};
console.log('person-olio', person);
// arvojen muuttaminen, molemmat käyvät
person['age'] = 35;
person.name = 'iines ankka';
// ominaisuuksien (property) lisääminen
person.profession = 'student';
console.log('person-olio', person);
// tiettyyn ominaisuuteen viittaaminen
console.log(person.name + ' on ' + person.age + '-vuotias.');


// metodin luominen olioon nimettömänä funktiona
const person2 = {
  name: 'iines',
  age: 34,
  getInfo: function () {
    return this.name + ' on ' + this.age + '-vuotias.'
  },
};

console.log(person2.getInfo());

// JS funktiot, 3 eri tapaa määritellä, keskitytään ensimmäiseen

function doSomething(name) {
  console.log('Moi ' + name);
}

const doSomething2 = function (name) {
  console.log('moi täältäkin', name);
};

const doSomething3 = (name) => {
  console.log('moiiii', name);
};

doSomething('Elli');
doSomething2('Kaisa');
doSomething3('Kirsi');

// lottorivin arvonta ja palautusarvo
// palautetaan rivi taulukkona esim. [3, 6, 5, 33, 35, 7, 27]

function lottoRivi(numberCount, maxValue) {
  const lotteryRow = [];
  while (lotteryRow.length < numberCount) {
    const number2 = Math.floor(Math.random() * maxValue + 1);
    if (!lotteryRow.includes(number2)) {
      lotteryRow.push(number2);
    }
    console.log('Pallon arvo: ' + number2);
  }
  return lotteryRow.sort((num1, num2) => num1-num2);
}

const myLotto = lottoRivi(7, 40);
console.log('My row', myLotto);
const myLotto2 = lottoRivi(9, 50);
console.log('My row', myLotto2);

// luodaan lottokuponki, jossa n määrä rivejä
function lotteryTicket(rowCount) {
  const ticket = [];
  for (let i=0; i<rowCount; i++) {
    const row = lottoRivi(7, 40)
    ticket.push(row);
  }
  return ticket;
}

const myTicket = lotteryTicket(5);
console.log(myTicket);
// tulostetaan 2. kupongin 3. numero
console.log(myTicket[1][2]);

// value scope / näkyvyysalue
// muuttuja2 on globaali, koska esitelty pääohjelmassa
let muuttuja2 = 2;
{
  const muuttuja = 0;
  muuttuja2 = 'uusi arvo';
  {
    const muuttuja = 'a';
    let muuttuja2 = 'vielä uudempi arvo';
    console.log(muuttuja2);
  }
  {
    console.log(muuttuja);
  }
}
console.log(muuttuja2);

// taulukko muuttujan parametrina
// uusi muuttuja numbers viittaa samaan taulukkoon kuin pääohjelman numbers

function arrayTest(numbers) {
  numbers.push(9);
  return numbers;
}

const numbers = [1, 2, 3];

console.log('Funktion paluuarvo', arrayTest(numbers));
console.log('alkuperäinen taulukko', numbers);

const numbers2 = numbers; // kopioidaan viittaus uuteen muuttujaan
console.log('kopioitu alkuperäinen taulukko', numbers2);


let numbers3 = []; // uuden taulukon luominen ja olemassaolevan taulukon yhdistäminen
numbers3 = numbers3.concat(numbers);
console.log('kopioidut taulukon arvot', numbers3);

// toinen tapa kopioida arvot uuteen taulukkoon (spread-operaattori)
const numbers4 = [...numbers]; // ...[1, 2, 3] => 1, 2, 3
console.log('myös kopioidut taulukon arvot', numbers4);