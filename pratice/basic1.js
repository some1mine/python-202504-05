const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function ladderUp(current, dice) {
    const next = current + dice;
    if (next == 4) {
        return next + 10;
    }
    else if (next == 8) {
        return next + 22;
    }
    else if (next == 28) {
        return next + 48;
    }
    else if (next == 21) {
        return next + 21;
    }
    else if (next == 50) {
        return next + 17;
    }
    else if (next == 71) {
        return next + 21;
    }
    else if (next == 80) {
        return next + 19;
    }
    
    return next;    
}

function snakeDown(next) {
    if(next == 97) {
        return next - 19;
    } 
    else if(next == 95) {
        return next - 39;
    } 
    else if(next == 88) {
        return next - 64;
    } 
    else if(next == 62) {
        return next - 44;
    } 
    else if(next == 48) {
        return next - 22;
    } 
    else if(next == 36) {
        return next - 30;
    } 
    else if(next == 32) {
        return next - 22;
    }

    return next;
}

let start = 1;
let next = 1;
let dice = 3;
next = ladderUp(start, dice);
next = snakeDown(next);
console.log("from=",start,", dice=",dice,", next=", next);

start = next;
dice = 4;
next = ladderUp(start, dice);
next = snakeDown(next);
console.log("from=",start,", dice=",dice,", next=", next);

start = next;
dice = 3;
next = ladderUp(start, dice);
next = snakeDown(next);
console.log("from=",start,", dice=",dice,", next=", next);

start = next;
dice = 5;
next = ladderUp(start, dice);
next = snakeDown(next);
console.log("from=",start,", dice=",dice,", next=", next);

start = next;
dice = 1;
next = ladderUp(start, dice);
next = snakeDown(next);
console.log("from=",start,", dice=",dice,", next=", next);
start = next;

function playTurn() {
    if (start >= 100) {
        console.log("You conquered the map!");
        rl.close();
        return;
    }

    rl.question(`current position : ${start}. Roll the dice? (y/n): `, (answer) => {
        if (answer === 'n') {
            rl.close();
            return;
        }
        const dice = Math.floor(Math.random() * 6) + 1;
        next = ladderUp(next, dice);
        next = snakeDown(next);
        console.log("from=",start,", dice=",dice,", next=", next);
        start = next;
        playTurn();
    });
}

playTurn();