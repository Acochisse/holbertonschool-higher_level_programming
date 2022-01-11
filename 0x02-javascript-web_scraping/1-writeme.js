#!/usr/bin/node

const filePath = process.argv[2];
const writeMe = process.argv[3];
const fs = require('fs');

fs.writeFile(filePath, writeMe, 'UTF-8', function (errorObj){
    if (errorObj) {
        console.log(errorObj);
    }
});