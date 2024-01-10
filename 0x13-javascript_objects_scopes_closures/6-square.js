#!/usr/bin/node
/* A class Square that defines a square and inherits from Rectangle */

const SquareParent = require('./5-square');

class Square extends SquareParent {
  /* class Square inherits from Square */
  constructor (size) {
  /* initialization of object */
    super(size, size);
  }

  charPrint (c) {
  /* prints the rectangle using the character c */
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
