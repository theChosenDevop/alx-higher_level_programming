#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      request.get(data[i], (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          const actors = JSON.parse(body);
          console.log(actors.name);
        }
      });
    }
  }
});
