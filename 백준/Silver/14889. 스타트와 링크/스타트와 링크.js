const fs = require('fs');
const [n, ...arr] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n');

const N = +n;

function startTeam(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      sum += stats[arr[i]][arr[j]];
    }
  }
  return sum;
}

function linkTeam(arr) {
  let linkArr = player.filter((v) => !arr.includes(v));
  let sum = 0;
  for (let i = 0; i < linkArr.length; i++) {
    for (let j = 0; j < linkArr.length; j++) {
      sum += stats[linkArr[i]][linkArr[j]];
    }
  }
  return sum;
}

function calcDiff(arr) {
  return Math.abs(startTeam(arr) - linkTeam(arr));
}

let player = [];
for (let i = 0; i < N; i++) {
  player.push(i);
}

let stats = arr.map((v) => v.split(' ').map((v) => +v));
let diff = 1000;

solve();
console.log(diff);

function countBits(value) {
  let count = 0;
  while (value > 0) {
    if ((value & 1) == 1) count++;
    value = value >> 1;
  }
  return count;
}

function solve() {
  const team = [];
  for (let i = 0; i < 1 << N; i++) {
    if (countBits(i) == N / 2) {
      let temp = [];
      for (let j = 0; j < N; j++) {
        if (i & (1 << j)) temp.push(j);
      }
      team.push(temp);
    }
  }
  team.forEach((v) => {
    if (calcDiff(v) < diff) diff = calcDiff(v);
  });
}