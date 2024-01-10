#!/usr/bin/node
/* create a class Rectangle and returns empty object
 * if constructor arguments are less than one */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
