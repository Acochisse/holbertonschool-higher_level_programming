#!/usr/bin/node
// script that returns the result of two args

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}
add(a, b);