#!/usr/bin/node

const fileStream = require('fs');
const file = process.argv[2];

fileStream.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
