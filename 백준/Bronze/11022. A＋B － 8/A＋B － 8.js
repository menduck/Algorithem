const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split('\n')
// const inputData = ['5','1 1','2 3','3 4','9 8','5 2'];

let caseN = parseInt(inputData[0]);
let result = '';

for(let i = 1 ; i < caseN +1 ; i++){
    let numbers = inputData[i].split(' ');
    let n = parseInt(numbers[0]) ;
    let m = parseInt(numbers[1]) ;
    let sum = n+m
    result += `Case #${i}: ${n} + ${m} = ${sum}\n`
   
}
console.log(result)