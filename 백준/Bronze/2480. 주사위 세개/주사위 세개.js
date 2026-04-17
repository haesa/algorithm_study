const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const dice = new Array(6).fill(0);
for (let i = 0; i < 3; i++) dice[input[i] - 1]++;

let answer = 0;
for (let i = 0; i < 6; i++) {
  if (dice[i] === 3) {
    answer = 10000 + (i + 1) * 1000;
    break;
  } else if (dice[i] === 2) {
    answer = 1000 + (i + 1) * 100;
    break;
  }
}
if (answer === 0) {
  let count = 0;
  for (let i = 0; i < 6; i++) {
    if (dice[i] !== 1) continue;
    count++;
    if (count === 3) {
      answer = (i + 1) * 100;
      break;
    }
  }
}

console.log(answer);