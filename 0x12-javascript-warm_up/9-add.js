#!/usr/bin/node

// sum two numbers
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(a + b);
}
