const fs = require('fs');
const [n, k] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const time = Array.from({length: 100001}, () => -1);

function solution() {
    const queue = [n];
    time[n] = 0;
    while(queue.length > 0) {
        const x = queue.shift();
        if(x - 1 >= 0 && time[x - 1] < 0) {
            time[x - 1] = time[x] + 1;
            queue.push(x - 1);
        }
        if(x + 1 <= 100000 && time[x + 1] < 0) {
            time[x + 1] = time[x] + 1;
            queue.push(x + 1);
        }
        if(x * 2 <= 100000 && time[x * 2] < 0) {
            time[x * 2] = time[x] + 1;
            queue.push(x * 2);
        }
    }
    
    console.log(time[k]);
}

solution();