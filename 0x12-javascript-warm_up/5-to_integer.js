#!/usr/bin/node

const process = require('process');
const convertArg = parseInt(process.argv[2]);
if (convertArg) {
  console.log(`My number: ${convertArg}`);
} else {
  console.log('Not a number');
}
