const [rc, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [r, c] = rc.trim().split(' ').map(Number);
const maze = input.map((s) => s.trim().split(''));
const fireDist = Array.from({ length: r }, () =>
  Array.from({ length: c }, () => -1)
);
const jihoonDist = Array.from({ length: r }, () =>
  Array.from({ length: c }, () => -1)
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

  length() {
    return this.size;
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
}

function isInvalidRange(x, y) {
  return x < 0 || x >= r || y < 0 || y >= c;
}

function fireBfs(queue) {
  while (queue.length() > 0) {
    const [x, y] = queue.pop();
    for (let k = 0; k < 4; k++) {
      const nx = x + dx[k];
      const ny = y + dy[k];
      if (isInvalidRange(nx, ny)) {
        continue;
      }
      if (fireDist[nx][ny] >= 0 || maze[x][y] === '#') {
        continue;
      }
      queue.push([nx, ny]);
      fireDist[nx][ny] = fireDist[x][y] + 1;
    }
  }
}

function jihoonBfs(queue) {
  while (queue.length() > 0) {
    const [x, y] = queue.pop();
    for (let k = 0; k < 4; k++) {
      const nx = x + dx[k];
      const ny = y + dy[k];
      if (isInvalidRange(nx, ny)) {
        return jihoonDist[x][y] + 1;
      }
      if (jihoonDist[nx][ny] >= 0 || maze[nx][ny] === '#') {
        continue;
      }
      if (fireDist[nx][ny] !== -1 && fireDist[nx][ny] <= jihoonDist[x][y] + 1) {
        continue;
      }
      queue.push([nx, ny]);
      jihoonDist[nx][ny] = jihoonDist[x][y] + 1;
    }
  }
  return 'IMPOSSIBLE';
}

function solution() {
  const fireQueue = new Queue();
  const jihoonQueue = new Queue();

  for (let i = 0; i < r; i++) {
    for (let j = 0; j < c; j++) {
      if (maze[i][j] === 'F') {
        fireQueue.push([i, j]);
        fireDist[i][j] = 0;
      }

      if (maze[i][j] === 'J') {
        jihoonQueue.push([i, j]);
        jihoonDist[i][j] = 0;
      }
    }
  }

  fireBfs(fireQueue);
  const result = jihoonBfs(jihoonQueue);
  console.log(result);
}

solution();
