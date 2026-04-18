const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, x] = input[0].split(' ').map((num) => +num);
const [...arr] = input[1].split(' ').map((num) => +num);
arr.forEach((num) => num < x && console.log(num));