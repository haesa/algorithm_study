const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = input[0];
input.splice(0, 1);
const operand = input.map((x) => x.split(' ').map(Number));

let answer = '';
for (let i = 0; i < n; i++) {
  const [a, b] = operand[i];
  answer += `${a + b} `;
}
console.log(answer);