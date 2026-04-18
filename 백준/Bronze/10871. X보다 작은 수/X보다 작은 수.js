const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().split('\n');

const input = inputs[0].split(' ');
const x = Number(input[1]);
const [...arr] = inputs[1].split(' ');
arr.forEach((num) => Number(num) < x && console.log(num));