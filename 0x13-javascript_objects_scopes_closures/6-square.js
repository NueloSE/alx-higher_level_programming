#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let row = 0; row < this.height; row++) {
        console.log(`${c}`.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
