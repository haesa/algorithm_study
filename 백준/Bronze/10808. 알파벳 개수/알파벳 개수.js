const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();

const alpha = new Array(26).fill(0);
for (const c of input) alpha[c.charCodeAt() - 97]++;

console.log(...alpha);