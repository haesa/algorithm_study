const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input.shift().split(' ').map(Number);

class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class Queue {
  constructor() {
    this.head = new Node([]);
    this.tail = this.head;
    this.size = 0;
  }

  push(data) {
    const node = new Node(data);
    this.tail.next = node;
    this.tail = node;
    this.size++;
  }

  shift() {
    if (this.size === 0) return;
    const node = this.head.next;
    if (node === this.tail) this.tail = this.head;
    this.head.next = node.next;
    this.size--;
    return node.data;
  }

  getSize() {
    return this.size;
  }
}

const map = [];
const map2 = [];
for (let i = 0; i < n; i++) {
  map.push(input[i].split(' ').map(Number));
  map2.push(input[i].split(' ').map(Number));
}

function isRange(x, y) {
  return x >= 0 && x < n && y >= 0 && y < m;
}

function bfs(i, j, visit) {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  const queue = new Queue();
  queue.push([i, j]);
  visit[i][j] = 1;
  while (queue.getSize()) {
    const [x, y] = queue.shift();
    for (let k = 0; k < 4; k++) {
      const nx = x + dx[k];
      const ny = y + dy[k];
      if (!isRange(nx, ny) || visit[nx][ny]) continue;
      if (map[nx][ny] === 0) map2[x][y]--;
      else {
        queue.push([nx, ny]);
        visit[nx][ny] = 1;
      }
    }
    if (map2[x][y] < 0) map2[x][y] = 0;
  }
}

function solution() {
  const visit = new Array(n);
  let year = 0;

  while (true) {
    let count = 0;
    for (let i = 0; i < n; i++) visit[i] = Array.from({ length: m }, () => 0);

    for (let i = 1; i < n - 1; i++)
      for (let j = 1; j < m - 1; j++) {
        if (map[i][j] === 0 || visit[i][j]) continue;
        bfs(i, j, visit);
        count++;
      }
    if (count > 1) return year;

    let melt = true;
    for (let i = 1; i < n - 1; i++)
      for (let j = 1; j < m - 1; j++) {
        map[i][j] = map2[i][j];
        if (map[i][j] !== 0) melt = false;
      }
    if (melt) return 0;
    year++;
  }
}
console.log(solution());