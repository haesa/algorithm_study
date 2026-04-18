const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());
const d = Array.from({ length: n + 1 }, () => 0);
const path = Array.from({ length: n + 1 }, () => 0);

d[1] = 0;
path[1] = [1];

for(let i = 2; i <= n; i++) {
    d[i] = d[i - 1] + 1;
    path[i] = [...path[i - 1], i];
    
    if(i % 3 === 0 && d[i / 3] + 1 < d[i]) {
        d[i] = d[i / 3] + 1;
        path[i] = [...path[i / 3], i];
    }
    if(i % 2 === 0 && d[i / 2] + 1 < d[i]) {
        d[i] = d[i / 2] + 1;
        path[i] = [...path[i / 2], i];
    }
}

console.log(d[n]);
console.log([...path[n]].reverse().join(' '));