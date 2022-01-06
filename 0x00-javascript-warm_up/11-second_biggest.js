#!/usr/bin/node
const lengthArg = process.argv.length;

if (lengthArg < 4) {
  console.log(0);
} else {
  const array = process.argv.slice(2);
  const secondBiggest = array.sort(function (i, j) {
    return j - i;
  })[1];
  console.log(secondBiggest);
}
