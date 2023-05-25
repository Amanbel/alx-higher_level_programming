#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const obj = {};
let n = 1;
let k = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const arr = JSON.parse(body);
    for (let i = 0; i < arr.length; i++) {
      for (let j = 0; j < arr.length; j++) {
        if (arr[j].userId === n) {
	  if (arr[j].completed === true) {
            k++;
	  }
	}
      }
      if (n <= 10) {
        obj[n] = k;
        k = 0;
        n++;
      }
    }
    console.log(obj);
  }
});
