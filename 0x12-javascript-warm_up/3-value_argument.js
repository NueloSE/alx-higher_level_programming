#!/usr/bin/node

const { argv } = require('process');

if (argv[2]) {
  for (let i = 2; argv[i] != undefined; i++) {
    console.log(`${argv[i]}`);
  }
} else {
  console.log('No argument');
}
