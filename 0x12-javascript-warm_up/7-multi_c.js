#!/usr/bin/node

const { argv } = require('process');

if (argv[2] === undefined) {
  console.log('Missing number of occurrences');
}

let numTimes = Number(argv[2]);

while (numTimes > 0) {
  console.log('C is fun');
  numTimes--;
}
