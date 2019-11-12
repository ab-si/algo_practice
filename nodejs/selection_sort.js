'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));
    main();
});

function readLine() {
    return inputString[currentLine++];
}

function selection_sort(a) {
    for (let i = 0; i < a.length - 1; i++) {
        let min = i
        for (let j = i+1; j < a.length; j++) {
            if (a[j] < a[min]){
                min = j
            }
        }
        let temp = a[i]
        a[i] = a[min]
        a[min] = temp
    }
    console.log(`Array : ${a}`);
}

function main() {
    // Send your input as "printf "1 2 3 5\n" | node filename.js"
    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));
    selection_sort(a);
}
