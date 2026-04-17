const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString());

let answer = '';
for (let i = 0; i < input; i++) {
  answer += ' '.repeat(i);
  answer += '*'.repeat(input - i);
  answer += '\n';
}
console.log(answer);