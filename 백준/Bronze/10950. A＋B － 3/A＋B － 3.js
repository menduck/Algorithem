const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split('\n') ;

const caseNum = parseInt(inputData[0]);

for(let i = 1 ; i < caseNum+1 ; i++){

    let result = inputData[i].split(' '); 
    console.log(parseInt(result[0])+parseInt(result[1]))
}
