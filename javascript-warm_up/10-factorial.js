#!/usr/bin/node
const { argv } = require('node:process');

function factorial(n){
    if (n === 0) {
        return 1;
    }
    return n * factorial(n - 1);
}

const num = parseInt(argv[2]);
if (isNaN(num)){
    console.log(1);
} else {
    console.log(factorial(num));
}
