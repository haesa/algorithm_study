const fs = require('fs');
const [n, ...scores] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);
const d = Array.from({length: n + 1}, () => 0);

d[1] = scores[0];
d[2] = scores[0] + scores[1];
d[3] = Math.max(scores[0] + scores[2], scores[1] + scores[2]);

for(let i = 4; i <= n; i++) {
    d[i] = Math.max(scores[i - 1] + scores[i - 2] + d[i - 3], scores[i - 1] + d[i - 2]);
}

console.log(d[n]);