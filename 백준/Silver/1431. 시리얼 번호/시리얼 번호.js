const fs = require('fs');
const [n, ...input] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const sum = (str) => {
  return str.match(/[\d]/g)?.reduce((acc, cur) => acc + Number(cur), 0) || 0;
};

input.sort((a, b) => {
  if (a.length !== b.length) {
    return a.length - b.length;
  }

  const aSum = sum(a);
  const bSum = sum(b);

  if (aSum !== bSum) {
    return aSum - bSum;
  }

  return a.localeCompare(b);
});

console.log(input.join('\n'));