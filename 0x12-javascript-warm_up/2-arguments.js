#!/usr/bin/node
let args = process.argv;
let out;
if (args.length == 2) {
	out = "No argument";
} else if (args.length == 3) {
	out = "Argument found";
} else if (args.length > 3) {
	out = "Arguments found";
}
console.log(out);
