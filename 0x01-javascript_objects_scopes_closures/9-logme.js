#!/usr/bin/node

let theCounter = 0;

exports.logMe = function (item) {
  console.log(theCounter + ': ' + item);
  theCounter++;
};
