const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const k = Number(input[0]);
const money = [];

for (let i = 1; i <= k; i++) {
  if (input[i] === '0') money.pop();
  else money.push(Number(input[i]));
}
console.log(money.reduce((acc, cur) => acc + cur, 0));