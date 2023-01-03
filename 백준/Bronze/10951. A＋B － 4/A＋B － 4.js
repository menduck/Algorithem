const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().trim().split("\n");
// const inputData = ['1 1','2 3','3 4','9 8','5 2']
const dataLength = inputData.length - 1 
let result = '';

for(let i = 0; i <= dataLength; i++){
    let splitedData = inputData[i].split(' ');
    let a = parseInt(splitedData[0]);
    let b = parseInt(splitedData[1]);
    let sum = a + b ;
    result += `${sum}\n`
} 
console.log(result.slice(0,-1));

