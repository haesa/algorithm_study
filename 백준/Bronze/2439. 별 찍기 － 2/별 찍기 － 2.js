const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString());

let answer = '';
for (let i = 1; i <= input; i++) {
  for (let j = input - i; j > 0; j--) answer += ' ';
  for (let j = 1; j <= i; j++) answer += '*';
  answer += '\n';
}
console.log(answer);