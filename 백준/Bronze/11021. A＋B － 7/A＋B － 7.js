const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split('\n')
// const inputData = ['5','1 1','2 3','3 4','9 8','5 2'];

let caseN = parseInt(inputData[0]);
let result = '';

for(let i = 1 ; i < caseN +1 ; i++){
    let numbers = inputData[i].split(' ');
    let m = parseInt(numbers[0])+parseInt(numbers[1])
    result += `Case #${i}: ${m}\n`
   
}
console.log(result)