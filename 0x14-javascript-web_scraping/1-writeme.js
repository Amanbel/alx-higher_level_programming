#!/usr/bin/node

const fileStream = require('fs');
const file = process.argv[2];
const content = process.argv[3];

fileStream.writeFile(file, content, (error) => {
  if (error) {
    console.log(error);
  }
})
