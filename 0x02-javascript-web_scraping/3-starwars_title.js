#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(url, function (errorId, response, body) {
  if (errorId) {
    console.log(errorId);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});