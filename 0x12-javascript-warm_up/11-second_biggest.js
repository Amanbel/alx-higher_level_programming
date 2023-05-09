#!/usr/bin/node

if (process.argv.length > 3) {
  let ord = process.argv.slice(2);
  let j = 0;
  let max = process.argv[2];
  for (let i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
      ord[j] = process.argv[i];
      j++;
    }
} else {
  console.log(0);
}
