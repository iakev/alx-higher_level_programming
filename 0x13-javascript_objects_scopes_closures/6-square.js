#!/usr/bin/node
const Square0 = require('./5-square');

class Square extends Square0 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        const letterArray = [];
        for (let j = 0; j < this.width; j++) {
          letterArray.push(c);
        }
        const squareLine = letterArray.join('');
        console.log(squareLine);
      }
    }
  }
}

module.exports = Square;
