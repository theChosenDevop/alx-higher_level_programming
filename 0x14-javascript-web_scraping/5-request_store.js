#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    fs.writeFileSync(file, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
