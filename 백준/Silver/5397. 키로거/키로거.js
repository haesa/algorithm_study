const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
let leftStack = [];
let rightStack = [];

for (let i = 1; i <= n; i++) {
  const pw = input[i];

  for (const c of pw) {
    switch (c) {
      case '<':
        leftStack.length && rightStack.push(leftStack.pop());
        break;
      case '>':
        rightStack.length && leftStack.push(rightStack.pop());
        break;
      case '-':
        leftStack.pop();
        break;
      default:
        leftStack.push(c);
    }
  }
  console.log(leftStack.join('') + rightStack.reverse().join(''));
  leftStack = [];
  rightStack = [];
}