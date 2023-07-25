#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let j = 0;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.results.length; ++i) {
      if (obj.results[i].characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        j++;
      }
    }
    console.log(j);
  }
});
