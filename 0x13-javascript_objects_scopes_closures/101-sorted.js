#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
for (let i = 0; i < Object.keys(dict).length; i++) {
  const holder = [];
  for (let j = 0; j < Object.keys(dict).length; j++) {
    if (Object.values(dict)[i] === Object.values(dict)[j]) {
      holder.push(Object.keys(dict)[j]);
    }
  }
  newDict[Object.values(dict)[i]] = holder;
}

console.log(newDict);
