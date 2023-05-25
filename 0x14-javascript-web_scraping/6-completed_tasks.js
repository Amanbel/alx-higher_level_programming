#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const obj = {};
let j = 1;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const arr = JSON.parse(body);
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].completed === true) {
        obj[j] = arr[i].id;
        j++;
      }
    }
    console.log(obj);
  }
});
