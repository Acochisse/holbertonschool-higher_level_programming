#!/usr/bin/node
// script that prints the number of args
const count = process.argv.length;
if (count === 2) {
  console.log('No argument');
} else if (count === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}