#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const url = process.argv[2];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
