let input = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(Number);

let max = Math.max(...input)

console.log(max)
console.log(input.indexOf(max) + 1)