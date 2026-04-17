const fs = require('fs');
const [str, n, ...cmd] = fs
  .readFileSync('/dev/stdin').toString().trim().split('\n');

const command = cmd.map((line) => line.trim().split(' '));
const leftStack = str.trim().split('');
const rightStack = [];

for (const line of command) {
  switch (line[0]) {
    case 'L':
      leftStack.length != 0 && rightStack.push(leftStack.pop());
      break;
    case 'D':
      rightStack.length != 0 && leftStack.push(rightStack.pop());
      break;
    case 'B':
      leftStack.length != 0 && leftStack.pop();
      break;
    case 'P':
      leftStack.push(line[1]);
      break;
  }
}
console.log(leftStack.join('') + rightStack.reverse().join(''));