#!/usr/bin/node
const Square = require('./5-square');

/*
 * A class Square that defines a square
 *and inherits from Square of 5-square.js
 */

class Square {
  contructor () {
    super()
  }

  charPrint(c) {
    if (c) {
      console.log('C');
    } else {
      console.log('X');
  }
}
