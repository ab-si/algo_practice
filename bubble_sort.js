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

function countSwaps(a) {
    let count = 0;
    for (let i=0; i<a.length; i++){
        for (let j=0; j<a.length; j++){
            if (a[j] > a[j+1]){
                let temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                count += 1
            }
        }
    }
    console.log(`Array is sorted in ${count} swaps.`);
    console.log(`First Element: ${a[0]}`);
    console.log(`Last Element: ${a[a.length-1]}`);
}

function main() {
    // Send your input as "printf "1 2 3 5\n" | node filename.js"
    const a = readLine().split(' ').map(aTemp => parseInt(aTemp, 10));
    countSwaps(a);
}
