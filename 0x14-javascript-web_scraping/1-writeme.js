#!/usr/bin/node

const fs = require('fs');

fs.writeFileSync(process.argv[2], process.argv[3], 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
