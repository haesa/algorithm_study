const fs = require('fs');
// const input = fs.readFileSync('./input/5397.txt').toString().trim().split('\n');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = +input.shift();

let left = [];
let right = [];

for(let i = 0; i < N; i++) {
	const pw = input[i];
	for(let j = 0; j < pw.length; j++) {
		const letter = pw[j];
		if (letter === '-' && left.length != 0) {
			left.pop();
		} else if (letter === '<' && left.length != 0) {
			right.push(left.pop());
		} else if (letter === '>' && right.length != 0) {
			left.push(right.pop());
		} else if (letter !== '-' && letter !== '<' && letter !== '>') {
			left.push(letter);
		}
	}
	console.log(left.join('')+right.reverse().join(''));
	left = [];
	right = [];
}