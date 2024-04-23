#!/usr/bin/node

const { argv } = require('process');

function factorial (num) {
  if (num === 1) { return 1; }
  return num * factorial(num - 1);
}

if (argv[2] === undefined) {
  console.log(1);
} else {
  const factNum = Number(argv[2]);
  console.log(factorial(factNum));
}
