#!/usr/bin/node

const { argv } = require('process')

function secondLargest(arr) {
	let first = arr[0];
	let second = -Infinity;
  
	for (let i = 1; i < arr.length; i++) {
	  if (arr[i] > first) {
		second = first;
		first = arr[i];
	  } else if (arr[i] > second && arr[i] < first) {
		second = arr[i];
	  }
	}
  
	return second;
  }
  
//   const numbers = [1, 10, 11, 3, 4, 5];
//   console.log(typeof numbers)
//   console.log(secondLargest(numbers));


const argvCpy = argv.slice(2)
console.log(argvCpy)

if (argv.length <= 3) {
  console.log(0);
} else {
	console.log(typeof argvCpy)
	console.log(secondLargest(argvCpy)); 
}
console.log('a')
console.log(4)