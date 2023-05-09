#!/usr/bin/node

if (process.argv.length > 3) {
  let max = Number(process.argv[2]);
  for (let i = 0; i < process.argv.length; i++) {
    if (Number(process.argv[i]) > max) {
      max = Number(process.argv[i]);
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
