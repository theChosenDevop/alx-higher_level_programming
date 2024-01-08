#!/usr/bin/node
/* script that prints a square */

const args = process.argv.slice(2);
const number = parseInt(args[0]);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  let j = 0;

  while (j < number) {
    console.log('X'.repeat(number));
    j++;
  }
}
