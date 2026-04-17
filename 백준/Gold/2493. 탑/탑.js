let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input.shift());
const tower = input[0].split(' ').map(Number);
const stack = [];
const result = [];

for (let i = 0; i < n; i++) {
  const curTower = tower[i];
  while (stack.length && tower[stack.at(-1)] < curTower) {
    stack.pop();
  }
  if (!stack.length) {
    result.push(0);
  } else {
    result.push(stack.at(-1) + 1);
  }
  stack.push(i);
}
console.log(result.join(' '));