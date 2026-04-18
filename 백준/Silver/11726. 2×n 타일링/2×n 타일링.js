const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());
const d = Array.from({ length: n + 1 }, () => 0);

d[1] = 1;
d[2] = 2;

for(let i = 3; i <= n; i++) {
    d[i] = (d[i - 1] + d[i - 2]) % 10007;
}

console.log(d[n]);