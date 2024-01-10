#!/usr/bin/node
/* A function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  let noccurence = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      noccurence++;
    }
  }
  return (noccurence);
};
