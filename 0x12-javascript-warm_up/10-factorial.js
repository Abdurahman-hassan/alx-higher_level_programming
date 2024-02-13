#!/usr/bin/node

// add factorial from arguments without function
const num = parseInt(process.argv[2]);
let result = 1;
for (let i = 1; i <= num; i++) {
  result *= i;
}
console.log(result);
