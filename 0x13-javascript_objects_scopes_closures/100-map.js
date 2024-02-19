#!/usr/bin/node

// Import the list from 100-data.js
const list = require('./100-data.js').list;

// Compute a new list where each value is the product of the initial value and its index
const newList = list.map((value, index) => value * index);

// Print the initial list and the new list
console.log(list);
console.log(newList);
