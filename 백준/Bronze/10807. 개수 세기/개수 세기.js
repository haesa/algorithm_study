const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = input[1].trim().split(' ');
console.log(arr.filter((x) => x === input[2]).length);