#!/usr/bin/node
const { argv } = require('node:process');

const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
