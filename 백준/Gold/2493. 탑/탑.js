let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

let n = Number(input[0]);
let tower = input[1].split(' ').map(Number);
let stack = [];
let result = [];

for (let i = 0; i < n; i++) {
  const curTower = tower[i];
  while (stack.length && tower[stack.at(-1)] < curTower) stack.pop();
  if (!stack.length) result.push(0);
  else result.push(stack.at(-1) + 1);
  stack.push(i);
}
console.log(...result);