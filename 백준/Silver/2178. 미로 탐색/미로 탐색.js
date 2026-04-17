const [nm, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = nm.split(' ').map(Number);
const maze = input.map((s) => s.trim().split('').map(Number));

const visit = new Array(n);
for (let i = 0; i < n; i++) visit[i] = Array.from({ length: m }, () => 0);

const dx = [0, 0, -1, 1];
const dy = [1, -1, 0, 0];

function isRange(x, y) {
  return x >= 0 && x < n && y >= 0 && y < m;
}

function isVisit(x, y) {
  return visit[x][y];
}

function solution() {
  const queue = [[0, 0, 1]];
  while (queue.length) {
    const cur = queue.shift();
    const [x, y, d] = cur;
    if (x + 1 === n && y + 1 === m) {
      console.log(d);
      break;
    }
    for (let k = 0; k < 4; k++) {
      const nx = x + dx[k];
      const ny = y + dy[k];
      if (!isRange(nx, ny) || isVisit(nx, ny) || maze[nx][ny] === 0) continue;
      visit[nx][ny] = 1;
      queue.push([nx, ny, d + 1]);
    }
  }
}
solution();