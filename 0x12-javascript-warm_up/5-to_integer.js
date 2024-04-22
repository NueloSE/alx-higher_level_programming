#!/usr/bin/node

const { argv } = require('process');

const num = Number(argv[2]);

if (num === Number(argv[2])) {
  console.log(`My number: ${Math.trunc(num)}`);
} else {
  console.log('Not a number');
}
