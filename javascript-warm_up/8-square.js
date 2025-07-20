#!/usr/bin/node
const { argv } = require('node:process');

const num = parseInt(argv[2]);
if (isNaN(num)) {
    console.log("Missing size");
} else {
    line = "X".repeat(num); 
for (let i = 0; i < num; i++){
    console.log(line);
}
}
