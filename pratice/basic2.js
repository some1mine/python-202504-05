function play(param0) {
    let arr  = [[10], [30], [50], [80]];
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

console.log(play([1,2,3]));
console.log(play([51,12,11,15,9,61]));
console.log(play([21,9,4]));
console.log(play([55,8,29,13,7,61]));