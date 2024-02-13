#!/usr/bin/node

const argLen = process.argv.length;
let processArg = parseInt(process.argv[2]);

if (argLen === 2 || isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
}

for (let i = 0; i < processArg; i++) {
    console.log('C is fun');
}
