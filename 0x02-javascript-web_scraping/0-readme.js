#!/usr/bin/node


const filePath = process.argv[2];
const fs = require('fs');

fs.readFile(filePath, 'UTF-8', function (errObj, fileContents) {
  if (errObj) {
    console.log(errObj);
  } else {
    console.log(fileContents.toString());
  }
});