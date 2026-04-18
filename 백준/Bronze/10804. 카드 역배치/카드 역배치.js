const fs = require('fs');
const [...input] = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map((x) => x.split(' ').map(Number));

const card = new Array(20).fill().map((_, i) => i + 1);

for (let i = 0; i < input.length; i++) {
  const [a, b] = input[i];
  const subArr = card.slice(a - 1, b).reverse();
  card.splice(a - 1, b - a + 1, ...subArr);
}

console.log(card.join(' '));