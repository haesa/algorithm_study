const [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const result = [];
const stack = [];

for (let i = 1, j = 0; i <= n; i++) {
  stack.push(i);
  result.push('+');
  while (stack.length && stack[stack.length - 1] === input[j]) {
    stack.pop();
    result.push('-');
    j++;
  }
}
if (stack.length) console.log('NO');
else console.log(...result);