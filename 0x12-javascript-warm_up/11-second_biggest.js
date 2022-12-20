#!/usr/bin/node

const process = require('process');
const argvLen = process.argv.length;
const argArr = [];

if (argvLen <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argvLen; i++) {
    const argInt = parseInt(process.argv[i]);
    argArr.push(argInt);
  }
  argArr.sort((a, b) => a - b);
  console.log(argArr[argArr.length - 2]);
}
