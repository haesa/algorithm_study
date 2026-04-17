const fs = require('fs');
const [num, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(num.trim());
const costs = input.map((s) => s.trim().split(' ').map(Number));
const d = Array.from({length: n}, () => Array.from({length: 3}, () => 0));

d[0][0] = costs[0][0];
d[0][1] = costs[0][1];
d[0][2] = costs[0][2];
for(let i = 1; i < n; i++) {
    d[i][0] = Math.min(d[i - 1][1], d[i - 1][2]) + costs[i][0];
    d[i][1] = Math.min(d[i - 1][0], d[i - 1][2]) + costs[i][1];
    d[i][2] = Math.min(d[i - 1][0], d[i - 1][1]) + costs[i][2];
}

const result = Math.min(d[n - 1][0], d[n - 1][1], d[n - 1][2]);
console.log(result);