#!/usr/bin/node

const url = process.argv[2];
const filePath = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, function (errorId, response, body){
if (errorId) {
    console.log(errorId);
} else {
    fs.writeFile(filePath, body, 'UTF-8', function (errorId){
        if (errorId) {
            console.log(errorId);
        }
    });
}
});