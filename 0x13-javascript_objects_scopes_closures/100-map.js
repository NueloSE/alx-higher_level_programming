#!/usr/bin/node

const list = require('./100-data').list;

const result = [];
for (let i = 0; i < list.length; i++) {
  result[i] = list[i] * i;
}

console.log(list);
console.log(result);
