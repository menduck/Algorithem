const fs = require('fs');
const inputData = fs
    .readFileSync(0,'utf8')
    .toString()
    .trim()
    .split('\n')
    
const caseN = parseInt(inputData[0])
const data = inputData[1]
    .split(" ")
    .map((i) => parseInt(i));

let min = data[0];
let max = data[0];
for(let i = 0; i<caseN;i++){
   if ( min > data[i]){
    min = data[i];
   }
   if ( max < data[i]){
    max = data[i];
   }
}
console.log(min,max)