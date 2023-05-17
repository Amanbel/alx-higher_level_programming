#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((a, ind) => {
  return a * ind;
});

console.log(list);
console.log(newList);
