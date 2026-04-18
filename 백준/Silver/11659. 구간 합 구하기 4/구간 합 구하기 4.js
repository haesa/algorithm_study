const fs = require('fs');
const [nt, input, ...input2] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, t] = nt.trim().split(' ').map(Number);
const numbers = input.trim().split(' ').map(Number);
const boundary = input2.map((s) => s.trim().split(' ').map(Number));
const d = Array.from({ length: n + 1 }, () => 0);

d[1] = numbers[0];

for(let i = 2; i <= n; i++) {
    d[i] = d[i - 1] + numbers[i - 1];
}

const result = [];
for(let i = 0; i < t; i++) {
    const [start, end] = boundary[i];
    result.push(d[end] - d[start - 1]);
}

console.log(result.join('\n'));