#!/usr/bin/node
let out;
if (process.argv.length == 2) {
	out = "No argument";
} else if (process.argv.length == 3) {
	out = "Argument found";
} else {
	out = "Arguments found";
}
console.log(out);
