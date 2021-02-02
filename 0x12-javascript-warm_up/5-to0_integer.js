#!/usr/bin/node
//script that determines if arg is a number and prints My number: argv[2]

const number = parseInt(process.argv[2]);
if (Number.isNaN(number)) {
    console.log('Not a number');
} else {
    console.log('My number: ' + number);
}
