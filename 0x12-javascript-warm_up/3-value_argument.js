#!/usr/bin/node
// if no args prints 'no args' else prints first arg

if (process.argv[2] === undefined) {
    console.log('No argument');
} else {
    console.log(process.argv[2]);
}
