const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
input.splice(0, 1);

let answer = '';
for (let i = 0; i < n; i++) {
  const [a, b] = input[i].split(' ').map(Number);
  answer += `${a + b} `;
}
console.log(answer);