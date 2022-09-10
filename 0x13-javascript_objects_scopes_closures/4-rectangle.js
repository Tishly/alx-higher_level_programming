#!/usr/bin/node

/*
 * A class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.name = 'Rectangle';
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = new Array(this.width).fill('X', 0, this.width);
    const rows = new Array(this.height).fill(row.join(''), 0, this.height);
    console.log(rows.join('\n'));
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
