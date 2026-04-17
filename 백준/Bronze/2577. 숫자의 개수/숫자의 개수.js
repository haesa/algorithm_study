const fs = require('fs');
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

const mult = input.reduce((acc, cur) => acc * cur);
const result = new Array(10).fill(0);

for (const c of mult.toString()) result[c.charCodeAt() - 48]++;

console.log(...result);