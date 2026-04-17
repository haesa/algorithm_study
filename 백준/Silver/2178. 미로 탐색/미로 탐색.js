const [nm, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = nm.split(' ').map(Number);
const maze = input.map((s) => s.trim().split('').map(Number));
const dist = Array.from({length: n}, () => Array.from({length: m}, () => 0));

const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

function bfs() {
    const queue = [[0, 0]];
    dist[0][0] = 1;
    while(queue.length > 0) {
        const [x, y] = queue.shift();
        for(let k = 0; k < 4; k++) {
            const nx = x + dx[k];
            const ny = y + dy[k];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m || maze[nx][ny] === 0 || dist[nx][ny] > 0) {
                continue;
            }
            queue.push([nx, ny]);
            dist[nx][ny] = dist[x][y] + 1;
        }
    }
}

function solution() {
    bfs();
    console.log(dist[n-1][m-1]);
}

solution();