#!/usr/bin/node

const SquareOg = require('./5-square');
class Square extends SquareOg {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(parseInt(this.width)));
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(parseInt(this.width)));
      }
    }
  }
}

module.exports = Square;
