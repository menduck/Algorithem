const fs = require('fs');
let inputData = fs.readFileSync(0,'utf8').toString().trim()
if (inputData.length ===1){
    inputData = '0'+inputData
}
let caseNum = 0 ;
let newNum = inputData;
//console.log(newNum)

while(true){
    let splitedInputData = Array.from(newNum) 
    let sum = (parseInt(splitedInputData[0]) + parseInt(splitedInputData[1])) % 10;//8 14
    newNum = splitedInputData[1] + sum.toString() // 68
    caseNum++
    if(newNum === inputData) break ;

}
console.log(caseNum);