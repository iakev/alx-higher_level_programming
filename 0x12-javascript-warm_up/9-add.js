#!/usr/bin/node

const process = require('process');
const firstArg = process.argv[2];
const secArg = process.argv[3];
const firstArgInt = parseInt(firstArg);
const secArgInt = parseInt(secArg);

function add (a, b) {
  const ans = a + b;
  console.log(ans);
}

add(firstArgInt, secArgInt);
