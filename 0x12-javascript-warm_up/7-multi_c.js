#!/usr/bin/node

let number = parseInt(process.argv[2]);

if (process.argv.length === 2 || isNaN(number)) {
    console.log('Missing number of occurrences');
} else {
    for (let i = 0; i < number; i++) {
        console.log('C is fun');
    }
}
