#!/usr/bin/node
/*Write to file from commandline*/

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error("Usage: ./writeme <filename> <data>");
}

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log("Data has been written to file successfully");
  }
});
