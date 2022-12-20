#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const firstArgInt = parseInt(firstArg);
const squareLetter = 'X';
let letterArray = [];

if (firstArgInt) {
  for (let i = 0; i < firstArgInt; i++) {
    for (let j = 0; j < firstArgInt; j++) {
      letterArray.push(squareLetter);
    }
    const squareLine = letterArray.join('');
    console.log(squareLine);
    letterArray = [];
  }
} else {
  console.log('Missing size');
}
