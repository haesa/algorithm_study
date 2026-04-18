const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const arr = input[1].split(' ').map(Number);
const x = Number(input[2]);

const check = new Array(1000001).fill(0);
let result = 0;
arr.forEach((num) => {
  check[x - num] && result++;
  check[num] = 1;
});

console.log(result);