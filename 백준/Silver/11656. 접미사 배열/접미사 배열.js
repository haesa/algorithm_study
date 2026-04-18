const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const answer = [];

for (let i = 0; i < input.length; i++) {
  answer.push(input.slice(i));
}

answer.sort();
console.log(answer.join('\n'));