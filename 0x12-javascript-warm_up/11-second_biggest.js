#!/usr/bin/node

const { argv } = require('process');

function secondBiggest (myArr) {
  let first = myArr[0];
  let second = -Infinity;

  for (let i = 2; i < myArr.length; i++) {
    if (myArr[i] > first) {
      second = first;
      first = myArr[i];
    } else if (myArr[i] > second && myArr[i] < first) {
      second = myArr[i];
    }
  }
  return second;
}

if (argv.length <= 3) {
  console.log(0);
} else { console.log(secondBiggest(argv)); }
