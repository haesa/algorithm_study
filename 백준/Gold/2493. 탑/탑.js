let fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');
let n  = Number(input.shift());
let arr = input[0].split(' ').map(Number)
let stack = []
let ans = [];

for (let i = 0; i < n; i++) {
    let now = arr[i]
    while(stack.length && arr[stack.at(-1)] < now) {
        stack.pop();
    }
    if (!stack.length) {
        ans.push(0)
    } else {
        ans.push(stack.at(-1) + 1)
    }
    stack.push(i)
}

console.log(ans.join(' '))