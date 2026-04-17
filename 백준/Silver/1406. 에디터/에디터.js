const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const leftStack = [...input[0].trim()];
const rightStack = [];

for (let i = 2; i < input.length; i++) {
  if (input[i][0] == 'L')
    leftStack.length != 0 && rightStack.push(leftStack.pop());
  else if (input[i][0] == 'D')
    rightStack.length != 0 && leftStack.push(rightStack.pop());
  else if (input[i][0] == 'B') leftStack.pop();
  else if (input[i][0] == 'P') leftStack.push(input[i][2]);
}

console.log(leftStack.join('') + rightStack.reverse().join(''));