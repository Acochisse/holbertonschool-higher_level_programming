#!/usr/bin/node
// script that prints the first arg passed
if (process.argv[2] === undefined) {
    console.log('no argument');
} else {
    console.log(process.argv[2])
}