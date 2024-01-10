#!/usr/bin/node
/* Defines a class Rectangle */

class Rectangle {
  constructor (w, h) {
  /* initialization of object */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
  /* print X character according to the width
     and height of rectangle */
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
  /* switch the width and height of rectangle */
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
  /* multiples the width and the height of the rectangle by 2 */
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
