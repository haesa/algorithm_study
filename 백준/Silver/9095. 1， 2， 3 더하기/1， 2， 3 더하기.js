const fs = require('fs');
const [_, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const dataList = input.map((num) => Number(num.trim()));
const d = Array.from({length: 11}, () => 0);
const answer = [];

d[1] = 1;
d[2] = 2;
d[3] = 4;
for(let i = 4; i <= 10; i++) {
    d[i] = d[i - 1] + d[i - 2] + d[i - 3];
}

dataList.forEach((data) => answer.push(d[data]));
console.log(answer.join('\n'));