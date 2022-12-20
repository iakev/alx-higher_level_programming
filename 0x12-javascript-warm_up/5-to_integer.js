#!/usr/bin/node

const process = require('process');
const lenArgv = process.argv.length;
let convertArg = parseInt(process.argv[2]);
if (convertArg){
  console.log(convertArg);
} else {
  console.log('Not a number');
}
