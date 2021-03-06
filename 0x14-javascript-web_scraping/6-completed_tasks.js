#!/usr/bin/node
// Script that determines the number of tasks

// a script that computes the number of tasks completed by user id

const url = process.argv[2];
const request = require('request');
const ret = {};

request(url, function (errorId, response, body) {
    if (errorId) {
	console.log(errorId);
    } else {
	for (const user of JSON.parse(body)) {
	    if (user.completed === true) {
		if (!(user.userId in ret)) {
		    ret[user.userId] = 1;
		} else {
		    ret[user.userId] = ret[user.userId] + 1;
		}
	    }
	}
    }
    console.log(reesesJSON);
});
