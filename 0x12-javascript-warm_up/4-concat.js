#!/usr/bin/node

const process = require('process');
const concatString = process.argv[2] + ' is ' + process.argv[3];
console.log(concatString);
