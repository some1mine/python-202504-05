// 데이터 입력/출력 부분
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function find(param0, param1) {
    books = [['Great',	true,	'Novel',	3.1,	2, 197001, 198104],
            ['Laws',	true,	'Novel',	4.8,	3, 198006, 198507],
            ['Dracula',	true,	'Drama',	2.3,	6, 199105, 199605],
            ['Mario',	true,	'Drama',	3.8,	4, 200109, 201211],
            ['House',	false,	'Magazine',	4.4,	1, 198707, 222212],
            ['Art1',	true,	'Design',	4.2,	2, 198506, 199107],
            ['Art2',	true,	'Design',	3.0,	3, 199502, 200512],
            ['Wars',	true,	'Novel',	4.6,	2, 198204, 200305],
            ['Solo',	false,	'Poem',	4.9,	2, 200703, 222212],
            ['Lost',	false,	'Web',	3.2,	8, 199806, 222212],
            ['Ocean',	true,	'Magazine',	4.3,	1, 200502, 202006]]
    results = ''
    for(let i = 0 ; i < books.length ; i++) {
        let book = books[i];
        if(book[4] >= param1 && book[5] <= param0 && book[6] >= param0) {
            results += book[0];
            if(book[1]) results += '*';
            results += '(' + book[2] + ') ';
            results += book[3] + ', ';
        }
    }
    if(results.length === 0) return "!EMPTY";
    return results.substring(0, results.length - 2);
}

function interact() {
    rl.question(`Input format is yearmonth, amount ex)200208, 4: `, (line) => {
        let inputs = line.trim().split(',');   
        if(inputs.length === 0) {
            rl.close(); 
            return;
        }
        const answer = find(parseInt(inputs[0]), parseInt(inputs[1]));
        console.log(answer);
        rl.close();
    });
}

interact();