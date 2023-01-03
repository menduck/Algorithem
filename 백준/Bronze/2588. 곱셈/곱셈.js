
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split("\n")
const A = inputData[0] ; 
const B = inputData[1] ; 
const str = String(B); 
const strArr = Array.from(str);

const result3 = A * parseInt(strArr[2]); 
const result4= A * parseInt(strArr[1]);
const result5 = A * parseInt(strArr[0]);
const result = A * B ;

console.log(`${result3}\n${result4}\n${result5}\n${result}`);