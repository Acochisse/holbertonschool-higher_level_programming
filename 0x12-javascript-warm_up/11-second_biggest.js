#!/usr/bin/node
// script that returns second largest int in a list

const lengthArg = process.argv.length;

if (lengthArg < 4) {
    console.log(0);
} else {
    const array = process.argv.slice(2);
    const secBig = array.sort(function (i, j) {
	return i - j;
    })[1];
    console.log(secBig);
}
