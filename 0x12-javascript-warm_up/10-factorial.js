#!/usr/bin/node
/* script that computes and prints a factorial */

const args = process.argv.slice(2);
const num = parseInt(args[0]);

function factorial (num) {
  if (isNaN(num) || num < 0) {
    return (1);
  } else if (num === 0 || num === 1) {
    return (1);
  } else {
    return (num * (factorial(num - 1)));
  }
}

console.log(factorial(num));
