#!/usr/bin/node

// A script that imports an array and computes a new array using map.

const list = require('./100-data').list;

// const result = [];
// for (let i = 0; i < list.length; i++) {
//   result[i] = list[i] * i;
// }

const newList = list.map((x) => x * list.indexOf(x));

console.log(list);
console.log(newList);
