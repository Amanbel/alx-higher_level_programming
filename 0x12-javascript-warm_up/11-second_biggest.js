#!/usr/bin/node

if (process.argv.length > 3) {
  let max = process.argv[2];
  for (let i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  const ord = process.argv.slice(2);
  const arr = ord.filter((item) => {
    if (item < max) {
      return Number(item);
    }
  });
  const secMax = arr.reduce((a, b) => Math.max(a, b), -Infinity);
  console.log(secMax);
} else {
  console.log(0);
}
