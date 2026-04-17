const [nm, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = nm.split(' ').map(Number);
const picture = input.map((s) => s.split(' ').map(Number));

const dx = [1, 0, -1, 0];
const dy = [0, 1, 0, -1];

function bfs (i, j) {
    const queue = [[i, j]];
    picture[i][j] = 0;
    let area = 0;
    while(queue.length > 0){
        const [x, y] = queue.shift();
        area += 1;
        for(let k = 0; k < 4; k++){
            const nx = x + dx[k];
            const ny = y + dy[k];
            if(nx < 0 || nx >= n || ny < 0 || ny >= m || picture[nx][ny] === 0){
                continue;
            }
            queue.push([nx, ny]);
            picture[nx][ny] = 0;
        }
    }
    return area;
}

function solution() {
    let count = 0;
    let max = 0;
    for(let i = 0; i < n; i++) {
        for(let j = 0; j < m; j++) {
            if(picture[i][j] === 0) {
                continue;
            }
            const size = bfs(i, j);
            max = size > max ? size : max;
            count += 1;
        }
    }
    console.log(count);
    console.log(max);
}

solution();