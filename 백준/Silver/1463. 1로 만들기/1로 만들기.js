const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString());
const d = Array.from({length: input + 1}, () => 0);

d[1] = 0;
for (let i = 2; i <= input; i++) {
  d[i] = d[i - 1] + 1;
  if (i % 2 === 0) {
    d[i] = Math.min(d[i], 1 + d[i / 2]);
  }
  if (i % 3 === 0) {
    d[i] = Math.min(d[i], 1 + d[i / 3]);
  }
}

console.log(d[input]);