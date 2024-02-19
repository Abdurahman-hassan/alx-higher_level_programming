#!/usr/bin/node

// Write a script that searches the second biggest integer in the list of arguments.
const arr = process.argv.slice(2).map(Number);
if (arr.length < 2) {
  console.log(0);
} else {
  // we sort the array in ascending order and then we get the second last element
  // 1 33 2 -> 1 2 33
  arr.sort((a, b) => a - b);
  // fetch the second last element
  console.log(arr[arr.length - 2]);
}
