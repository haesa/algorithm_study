const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let answer = [];
for (const input of inputs) {
  let stick = 0;
  const arr = input.split(' ').map(Number);
  arr.forEach((a) => (stick += a));
  switch (stick) {
    case 0:
      answer.push('D');
      break;
    case 1:
      answer.push('C');
      break;
    case 2:
      answer.push('B');
      break;
    case 3:
      answer.push('A');
      break;
    case 4:
      answer.push('E');
  }
}

console.log(answer.join('\n'));