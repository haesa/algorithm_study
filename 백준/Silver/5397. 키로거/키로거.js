const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);

for (let i = 1; i <= n; i++) {
  const leftStack = [];
  const rightStack = [];

  for (const c of input[i]) {
      if(c === '<') leftStack.length && rightStack.push(leftStack.pop());
      else if(c === '>') rightStack.length && leftStack.push(rightStack.pop());
      else if(c === '-') leftStack.pop();
      else leftStack.push(c);
  }
  console.log(leftStack.join('') + rightStack.reverse().join(''));
}