const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input.shift());

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

let visit;

let h, w;

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

let fireQ;
let escapeQ;

function isRange(x, y) {
  return x >= 0 && x < h && y >= 0 && y < w;
}

function bfs() {
  while (fireQ.getSize() || escapeQ.getSize()) {
    for (let i = fireQ.getSize(); i > 0; i--) {
      const [x, y] = fireQ.shift();
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (!isRange(nx, ny) || visit[nx][ny] === 1) continue;
        fireQ.push([nx, ny]);
        visit[nx][ny] = 1;
      }
    }

    for (let i = escapeQ.getSize(); i > 0; i--) {
      const [x, y, d] = escapeQ.shift();
      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (!isRange(nx, ny)) return d + 1;
        if (visit[nx][ny]) continue;
        escapeQ.push([nx, ny, d + 1]);
        visit[nx][ny] = 2;
      }
    }
  }
  return 'IMPOSSIBLE';
}

function soluition() {
  const answer = [];

  for (let t = 0; t < n; t++) {
    fireQ = new Queue();
    escapeQ = new Queue();
    [w, h] = input.shift().split(' ').map(Number);

    const map = [];
    for (let i = 0; i < h; i++) map.push(input.shift().trim().split(''));

    visit = new Array(h);
    for (let i = 0; i < h; i++) visit[i] = Array.from({ length: w }, () => 0);

    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        if (map[i][j] === '*') {
          fireQ.push([i, j, 0]);
          visit[i][j] = 1;
        } else if (map[i][j] === '@') {
          escapeQ.push([i, j, 0]);
          visit[i][j] = 2;
        } else if (map[i][j] === '#') visit[i][j] = 1;
      }
    }
    answer.push(bfs());
  }
  console.log(answer.join(' '));
}
soluition();