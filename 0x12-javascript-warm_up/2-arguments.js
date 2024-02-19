#!/usr/bin/node
const argCount = process.argv.length;
console.log(argCount === 2 ? 'No argument' : argCount === 3 ? 'Argument found' : 'Arguments found');
