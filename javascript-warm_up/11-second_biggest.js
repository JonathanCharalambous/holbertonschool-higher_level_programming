#!/usr/bin/node
const { argv } = require('node:process');
let largest = 0;
let secondLargest = 0;

argv.forEach((val) => {
  const num = parseInt(val);
  if (num > largest) {
    secondLargest = largest;
    largest = num;
  } else if (num > secondLargest) {
    secondLargest = num;
  }
});
console.log(secondLargest);
