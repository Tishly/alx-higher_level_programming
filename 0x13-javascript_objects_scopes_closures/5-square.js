#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/*
 * A class Square that defines a square and
 *inherits from Rectangle of 4-rectangle.js
 */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.name = 'Square';
  }
}
module.exports = Square;
