#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const requestUrl = process.argv[2];
const filePath = process.argv[3];

request(requestUrl, (err, response, body) => {
  if (err) {
    throw (err);
  }
  fs.writeFile(filePath, body, 'utf8', (err, data) => {
    if (err) {
      throw (err);
    }
  });
});
