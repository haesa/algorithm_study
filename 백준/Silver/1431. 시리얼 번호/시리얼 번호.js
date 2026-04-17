const fs = require('fs');
const stdin = fs.readFileSync('/dev/stdin').toString().split('\n');
const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = +input();
let arr = [];

while (N--) arr.push(input());

arr.sort((a, b) => {
  if (a.length != b.length) return a.length - b.length;
  let sum1 = sum(a),
    sum2 = sum(b);
  if (sum1 == sum2) return a.localeCompare(b);
  return sum1 - sum2;
});

console.log(arr.join('\n'));

function sum(str) {
  return str.match(/[\d]/g)?.reduce((sum, cur) => sum + +cur, 0) || 0;
}