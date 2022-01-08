#!/usr/bin/node

const dict = require('./101-data.js').dict;

const result = {};
for (const k in dict) {
  result[dict[k]] = [];
}

for (const k in dict) {
  result[dict[k]].push(k);
}

console.log(result);
