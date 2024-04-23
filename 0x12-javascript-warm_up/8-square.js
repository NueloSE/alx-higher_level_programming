#!/usr/bin/node

const { argv } = require('process');

if (argv[2] === undefined) { console.log('Missing size'); }
const squareSize = Number(argv[2]);
for (let row = 0; row < squareSize; row++) {
  console.log('X'.repeat(squareSize));
}
