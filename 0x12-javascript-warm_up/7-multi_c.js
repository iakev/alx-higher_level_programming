#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const firstArgInt = parseInt(firstArg);
if (firstArgInt) {
  for (let i = 0; i < firstArgInt; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
