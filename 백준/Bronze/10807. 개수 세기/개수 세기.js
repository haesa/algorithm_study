const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input.shift());
const arr = input.shift().split(' ').map(Number);
const v = Number(input[0]);
console.log(arr.filter((x) => x === v).length);