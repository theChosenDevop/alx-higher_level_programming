#!/usr/bin/node
/* A class Square that defines a square and inherits from Rectangle */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /* defines class Square */
  constructor (size) {
  /* initialization of object */
    super(size, size);
  }
}

module.exports = Square;
