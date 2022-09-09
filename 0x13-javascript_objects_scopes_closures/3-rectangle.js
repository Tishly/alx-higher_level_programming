#!/usr/bin/node

/*
 * A class Rectangle that defines a rectangle
 */

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stringToDisplay = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        stringToDisplay += 'x';
      }
      stringToDisplay += '\n'
    }
    console.log(stringToDisplay);
  }
}
module.exports = Rectangle;
