#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const myJSON = {};

request(url, function (errorId, response, body) {
  if (errorId) {
    console.log(errorId);
  } else {
    for (const user of JSON.parse(body)) {
      if (user.completed === true) {
        if (!(user.userId in myJSON)) {
          myJSON[user.userId] = 1;
        } else {
          myJSON[user.userId] = myJSON[user.userId] + 1;
        }
      }
    }
  }
  console.log(myJSON);
});