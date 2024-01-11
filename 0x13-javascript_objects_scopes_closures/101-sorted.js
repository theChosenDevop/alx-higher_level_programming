#!/usr/bin/node
/* A script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */

const { dict } = require('./101-data');

const occurrencesDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (occurrence in occurrencesDict) {
    occurrencesDict[occurrence].push(parseInt(userId));
  } else {
    occurrencesDict[occurrence] = [parseInt(userId)];
  }
}

console.log(occurrencesDict);
