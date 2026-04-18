const [mn, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [m, n] = mn.split(' ').map(Number);
const tomatos = input.map((s) => s.trim().split(' ').map(Number));
const dist = Array.from({ length: n }, () =>
  Array.from({ length: m }, () => 0)
);

const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

class Node {
  constructor(item) {
    this.item = item;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(item) {
    const node = new Node(item);
    if (this.size === 0) {
      this.head = node;
    } else {
      this.tail.next = node;
    }
    this.tail = node;
    this.size += 1;
  }

  pop() {
    const node = this.head;
    this.head = node.next;
    this.size -= 1;
    return node.item;
  }

  length() {
    return this.size;
  }
}

function bfs(queue) {
  while (queue.length() > 0) {
    const [x, y] = queue.pop();
    for (let k = 0; k < 4; k++) {
      const nx = x + dx[k];
      const ny = y + dy[k];
      if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
        continue;
      }
      if (dist[nx][ny] >= 0) {
        continue;
      }
      queue.push([nx, ny]);
      dist[nx][ny] = dist[x][y] + 1;
    }
  }
}

function solution() {
  const queue = new Queue();

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (tomatos[i][j] === 1) {
        queue.push([i, j]);
      }
      if (tomatos[i][j] === 0) {
        dist[i][j] = -1;
      }
    }
  }

  bfs(queue);

  let result = 0;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (dist[i][j] === -1) {
        console.log(-1);
        return;
      }
      result = dist[i][j] > result ? dist[i][j] : result;
    }
  }
  console.log(result);
}

solution();