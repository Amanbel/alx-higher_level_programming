#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
let characters = [];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charsArr = JSON.parse(body).characters;
    for (let i = 0; i < charsArr.length; i++) {
      request(charsArr[i], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          characters.push(JSON.parse(body).name);
        }
      });
    }
    for (let i = 0; i < characters.length; i++) {
      console.log(characters[i]);
    }
  }
});
