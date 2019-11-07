'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the migratoryBirds function below.
function migratoryBirds(arr) {
    let c = new Array(arr.length).fill(0);
    for (let i = 0;i<arr.length;i++) {
        c[arr[i]] += 1;
    }
    return c.indexOf(c.reduce((a,b)=>Math.max(a,b)));
}
function main() {
    /*
    You have been asked to help study the population of birds migrating across the continent.
    Each type of bird you are interested in will be identified by an integer value.
    Each time a particular kind of bird is spotted,
    its id number will be added to your array of sightings.
    You would like to be able to find out which type of bird is most common given a list of sightings.
    Your task is to print the type number of that bird and if two or more types of birds
    are equally common, choose the type with the smallest ID number.
    */    
    const arrCount = parseInt(readLine().trim(), 10);
    const arr = readLine().replace(/\s+$/g, '').split(' ').map(arrTemp => parseInt(arrTemp, 10));
    const result = migratoryBirds(arr);
    console.log(result);
}
