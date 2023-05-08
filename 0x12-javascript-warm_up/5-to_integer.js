#!/usr/bin/node

if (process.argv[2]) {
  if (Number(process.argv[2])) {
    console.log('My number: ' + process.argv[2]);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
