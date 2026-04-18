const fs = require('fs');
const [n, ...str] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

for (const s of str) {
  const leftStack = [];
  const rightStack = [];

  for (const c of s) {
    switch (c) {
      case '<':
        leftStack.length > 0 && rightStack.push(leftStack.pop());
        break;
      case '>':
        rightStack.length > 0 && leftStack.push(rightStack.pop());
        break;
      case '-':
        leftStack.pop();
        break;
      default:
        leftStack.push(c);
    }
  }
  console.log(leftStack.join('') + rightStack.reverse().join(''));
}