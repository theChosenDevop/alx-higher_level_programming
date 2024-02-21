#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body);
    const counts = {};

    data.forEach(item => {
      const userId = item.userId;
      if (!counts[userId]) {
        counts[userId] = 0;
      }
      if (item.completed) {
        counts[userId]++;
      }
    });
    console.log(counts);
  }
});
