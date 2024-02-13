#!/usr/bin/node

let processArg = parseInt(process.argv[2]);

if (process.argv.length === 2 || isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < processArg; i++) {
        console.log('C is fun');
    }
}
