const fs = require('fs');
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

let max = 0;
let index;
input.forEach((num, i) => num > max && ((max = num), (index = i + 1)));
console.log(`${max}\n${index}`);