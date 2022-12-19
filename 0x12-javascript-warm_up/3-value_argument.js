#!/usr/bin/node

const process = require('process');
let finalIndex = 0;

process.argv.forEach((val, index) => {
  if (index > 1) {
    console.log(val);
  }
  finalIndex = index;
});
if (finalIndex < 1) {
  console.log('No argument');
}
