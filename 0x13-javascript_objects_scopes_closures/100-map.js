#!/usr/bin/node

// A script that imports an array and computes a new array using map.

const list = require('./100-data').list;

const newList = list.map((element, indx) => element * indx);

console.log(list);
console.log(newList);
