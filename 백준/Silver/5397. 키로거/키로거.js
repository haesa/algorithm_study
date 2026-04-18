const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
let leftStack;
let rightStack;

for (let i = 1; i <= n; i++) {
  const pw = input[i];
  leftStack = [];
  rightStack = [];
    
  for (const c of pw) {
    switch (c) {
      case '<':
        if(leftStack.length) rightStack.push(leftStack.pop());
        break;
      case '>':
        if(rightStack.length) leftStack.push(rightStack.pop());
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