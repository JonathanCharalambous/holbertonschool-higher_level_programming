#!/usr/bin/node
const { argv } = require('node:process');
const num = parseInt(argv[2]) + parseInt(argv[3]);
if (isNaN(num)) {
    console.log("NaN");
} else {
    console.log(num);
}