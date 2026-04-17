const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);

class Node {
  constructor(x, y) {
    this.x = x;
    this.y = y;
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
  push(x, y) {
    let node = new Node(x, y);
    if (this.size === 0) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.size++;
  }
  pop() {
    let temp = this.head;
    if (this.size === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head.next;
    }
    this.size--;
    return temp;
  }
}
function sol(map, map2, i, j, visited) {
  let dx = [0, 0, -1, 1];
  let dy = [-1, 1, 0, 0];

  let q = new Queue() // x,y
  q.push(j, i);
  visited[i][j] = true;
  while (q.length()) {
    let cur = q.pop();
    let [cx, cy] = [cur.x, cur.y];
    for (let next = 0; next < 4; next++) {
      let [nx, ny] = [cx + dx[next], cy + dy[next]];
      if (nx >= M || nx < 0 || ny >= N || ny < 0) continue;
      else {
        if (!visited[ny][nx] && map[ny][nx]) {
          q.push(nx, ny);
          visited[ny][nx] = true;
        }
        if (map[ny][nx] === 0) { // 주변이 바다면 빙하가 녹는다.
          map2[cy][cx]--;
          if (map2[cy][cx] < 0) map2[cy][cx] = 0; // 높이는 0보다 줄어들지 않는다.
        }
      }
    }
  }
}
function main() {
  let answer = 0;

  let map = [];
  let map2 = [];
  for (let i = 1; i <= N; i++) {
    map.push(input[i].split(' ').map(Number)); // 원본.
    map2.push(input[i].split(' ').map(Number)); // 업데이트용.
  }

  let cnt = 0; // 빙산이 몇조각인지.
  while (1) {
    let visited = new Array(N).fill(null).map(_ => new Array(M).fill(false));
    cnt = 0;
    for (let i = 1; i < N - 1; i++) {
      for (let j = 1; j < M - 1; j++) {
        if (map[i][j] !== 0 && !visited[i][j]) {
          sol(map, map2, i, j, visited);
          cnt++;
        }
      }
    }
    if (cnt >= 2) {
      //console.log(map2)
      break;
    } // 빙산이 분리됐을경우 종료.

    let check = true; // 빙산이 다 녹았을 경우.
    for (let y = 1; y < N - 1; y++) { // 빙하가 녹은 정보를 업데이트한다.
      for (let x = 1; x < M - 1; x++) {
        map[y][x] = map2[y][x];
        if (map[y][x] !== 0) check = false;
      }
    }
    if (check) return console.log(0); // 얼음이 다 녹았을 경우.
    answer++;
  }
  console.log(answer);
}
main();