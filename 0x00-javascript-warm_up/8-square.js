#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let count = 0; count < x; count++) {
    console.log('X'.repeat(x));
  }
}