const fs = require('fs');
const [n, ...str] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

let leftStack;
let rightStack;

const moveLeft = () => leftStack.length > 0 && rightStack.push(leftStack.pop());
const moveRight = () =>
  rightStack.length > 0 && leftStack.push(rightStack.pop());

for (const s of str) {
  leftStack = [];
  rightStack = [];

  for (const c of s) {
    switch (c) {
      case '<':
        moveLeft();
        break;
      case '>':
        moveRight();
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