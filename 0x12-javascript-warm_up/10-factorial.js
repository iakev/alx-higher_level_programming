#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const firstArgInt = parseInt(firstArg);

function factorial (n) {
  if (!n) {
    return 1;
  } else {
    if (n === 1) {
      return n;
    } else {
      return n * factorial(n - 1);
    }
  }
}

const fact = factorial(firstArgInt);
console.log(fact);
