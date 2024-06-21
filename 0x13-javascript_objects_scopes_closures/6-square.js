#!/usr/bin/node
const oldSquare = require('./5-square');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    // this.print();
    for (let row = 0; row < this.height; row++) { console.log(`${c}`.repeat(this.width)); }
  }
}

module.exports = Square;
