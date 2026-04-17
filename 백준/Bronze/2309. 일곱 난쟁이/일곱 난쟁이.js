const fs = require('fs');
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

input.sort((a, b) => a - b);

const sub = input.reduce((acc, cur) => acc + cur, 0) - 100;

for (let i = 0; i < 8; i++)
  for (let j = i + 1; j < 9; j++)
    if (input[i] + input[j] == sub) {
      const result = input
        .filter((height) => height != input[i] && height != input[j])
        .join('\n');
      console.log(result);
      return 0;
    }