const fs = require('fs');
const [n, ...input] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');
const answer = input.map((v) => v.trim());
const sum = (str) => {
  return str.match(/[\d]/g)?.reduce((acc, cur) => acc + Number(cur), 0) || 0;
};

answer.sort();
answer.sort((a, b) => {
  if (a.length !== b.length) {
    return a.length - b.length;
  }

  const aSum = sum(a);
  const bSum = sum(b);

  if (aSum !== bSum) {
    return aSum - bSum;
  }
});

console.log(answer.join('\n'));