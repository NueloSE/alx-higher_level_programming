#!/usr/bin/node

const { argv } = require('process');

const squareSize = Number(argv[2]);

if (Number(argv[2]) !== squareSize) { console.log('Missing size'); }
for (let row = 0; row < squareSize; row++) {
  console.log('X'.repeat(squareSize));
}
