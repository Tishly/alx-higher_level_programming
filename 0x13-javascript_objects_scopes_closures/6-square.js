#!/usr/bin/node

/*
 * A class Square that defines a square
 *and inherits from Square of 5-square.js
 */

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let k = 0; k < this.height; k++) console.log(c.repeat(this.width));
    }
  }
};
