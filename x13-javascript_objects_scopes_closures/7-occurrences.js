#!/usr/bin/node
/* A function that returns the number of occurrences in a list */

exports.nb0ccurences = function nb0ccurences (list, searchElement) {
  let noccurence = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      noccurence++;
    }
  }
  return (noccurence);
};
