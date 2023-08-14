#!/usr/bin/node

const args = process.argv;
const sorted = args.sort((a, b) => a - b);

sorted.shift();
if (args.length < 3) {
  console.log(0);
} else {
  console.log(sorted[sorted.length - 2]);
}
