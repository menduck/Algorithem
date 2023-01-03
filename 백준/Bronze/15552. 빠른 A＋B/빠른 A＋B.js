const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split('\n')
// const inputData = ['5','1 1','12 34','5 500','40 60','1000 1000'];

let caseN = parseInt(inputData[0]);
let result = '';

for(let i = 1 ; i < caseN +1 ; i++){
    let numbers = inputData[i].split(' ');
    result += parseInt(numbers[0])+parseInt(numbers[1])+'\n'
    
}
console.log(result)