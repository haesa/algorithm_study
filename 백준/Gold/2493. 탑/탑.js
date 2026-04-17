const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const tower = input[1].split(' ').map(Number);
const stack = [[100000001, 0]];
const result = [];

for (let i = 0; i < n; i++) {
  while (stack[stack.length - 1][0] < tower[i]) stack.pop();
  result.push(stack[stack.length - 1][1]);
  stack.push([tower[i], i + 1]);
}
console.log(...result);