#!/usr/bin/node

const process = require('process');

const variables = process.argv.length;
if (variables <= 2) {
  console.log('No argument');
} else if (variables === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
