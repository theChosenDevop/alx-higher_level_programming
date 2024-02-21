#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

function printCharacterNames (characterUrls, index) {
  if (index >= characterUrls.length) {
    return;
  }

  const characterUrl = characterUrls[index];
  request.get(characterUrl, (err, res, body) => {
    if (err) {
      console.error(err);
    } else {
      const charactersData = JSON.parse(body);
      console.log(charactersData.name);
      printCharacterNames(characterUrls, index + 1);
    }
  });
}

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;

    printCharacterNames(characters, 0);
  }
});
