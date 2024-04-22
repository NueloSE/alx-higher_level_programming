#!/usr/bin/env node

const { argv } = require('node:process');

if (argv[2]) {
  for (let i = 2; argv[i]; i++) {
    console.log(`${argv[i]}`);
  }
} else {
  console.log('No argument');
}
