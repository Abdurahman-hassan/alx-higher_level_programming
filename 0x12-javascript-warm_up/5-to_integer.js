#!/usr/bin/node
const args = process.argv.slice(2);
console.log(isNaN(args[0]) ? 'Not a number' : 'My number: ' + args[0]);
