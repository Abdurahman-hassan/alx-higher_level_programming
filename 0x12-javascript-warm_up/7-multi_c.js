#!/usr/bin/node

const argLen = process.argv.length;

if (argLen === 2 || isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
}

let processArg = parseInt(process.argv[2]);

for (let i = 0; i < processArg; i++) {
    console.log('C is fun');
}
