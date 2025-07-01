function play(arr, param0) {
    function findOrd(num) {
        let diff = 99999; let idx = -1;
        for(let i = 0 ; i < 4 ; i++) {
            if(arr[i].length > 0 && Math.abs(num - arr[i][arr[i].length - 1]) < diff) {
                idx = i; diff = Math.abs(num - arr[i][arr[i].length - 1]);
            }
        }
        return idx;
    }
    results = [0, 0, 0];
    for(let i = 0 ; i < param0.length / 3 ; i++) {
        let max = Math.max(param0[i * 3], param0[i * 3 + 1], param0[i * 3 + 2]);
        let min = Math.min(param0[i * 3], param0[i * 3 + 1], param0[i * 3 + 2]);
        let mid = -1;
        let maxIdx = -1; let minIdx = -1; let midIdx = -1;
        for(let j = 0 ; j < 3 ; j++) {
            if(max == param0[i * 3 + j]) {
                maxIdx = i * 3 + j;
            } else if(min == param0[i * 3 + j]) {
                minIdx = i * 3 + j;
            } else {
                midIdx = i * 3 + j; mid = param0[i * 3 + j];
            }
        }
        let minOrd = findOrd(min); let maxOrd = findOrd(max); let midOrd = findOrd(mid);
        if(arr[minOrd].length > 0) {
            if(arr[minOrd][arr[minOrd].length - 1] > min) {
                arr[minOrd].push(min);
            } else {
                results[minIdx % 3] += arr[minOrd].length; arr[minOrd] = [];
            }            
        }
        if(arr[midOrd].length > 0) {
            if(arr[midOrd][arr[midOrd].length - 1] > mid) {
                arr[midOrd].push(mid);
            } else {
                results[midIdx % 3] += arr[midOrd].length; arr[midOrd] = [];
            }            
        }
        if(arr[maxOrd].length > 0) {
            if(arr[maxOrd][arr[maxOrd].length - 1] > max) {
                arr[maxOrd].push(max);
            } else {
                results[maxIdx % 3] += arr[maxOrd].length; arr[maxOrd] = [];
            }            
        }
    }
    return new Map([['A', results[0]], ['B', results[1]], ['C', results[2]]]);
}

let arr  = [[10], [30], [50], [80]];
if(arr[0].length == 0 && arr[1].length == 0 && arr[2].length == 0 && arr[3].length == 0) {
    rl.close();
    return;
}
console.log(play(arr, [1,2,3]));
arr  = [[10], [30], [50], [80]];
if(arr[0].length == 0 && arr[1].length == 0 && arr[2].length == 0 && arr[3].length == 0) {
    rl.close();
    return;
}
console.log(play(arr, [51,12,11,15,9,61]));
arr  = [[10], [30], [50], [80]];
if(arr[0].length == 0 && arr[1].length == 0 && arr[2].length == 0 && arr[3].length == 0) {
    rl.close();
    return;
}
console.log(play(arr, [21,9,4]));
arr  = [[10], [30], [50], [80]];
if(arr[0].length == 0 && arr[1].length == 0 && arr[2].length == 0 && arr[3].length == 0) {
    rl.close();
    return;
}
console.log(play(arr, [55,8,29,13,7,61]));



// 데이터 입력/출력 부분
const readline = require('readline');
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

let cards = []; let A = []; let B = []; let C = [];
for(let i = 1 ; i <= 100 ; i++) {
    if(i === 10 || i === 30 || i === 50 || i === 80) continue;
    cards.push(i);
}
for(let i = 0 ; i < 10 ; i++) {
    A.push(cards[i]); B.push(cards[i * 3]); C.push(cards[i * 6]);
}

function playTurn() {
    let arr  = [[10], [30], [50], [80]];
    if(arr[0].length == 0 && arr[1].length == 0 && arr[2].length == 0 && arr[3].length == 0) {
        rl.close();
        return;
    }
    rl.question(`Input choice of A, B, C (Count of numbers must be multiple of 3 and splited by comma(,)): `, (line) => {
        let inputs = line.trim();   
        if(inputs.length === 0) {
            rl.close(); 
            return;
        }
        const numArray = inputs.split(',').map(Number);
        const answer = play(arr, numArray);
        for (const [key, value] of answer){
            console.log(key+"="+value);
        }
        playTurn();
    });
}

playTurn();