const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");
const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);
const C = parseInt(inputData[2]);

const result1 = (A+B)%C ;
const result2 = ((A%C) + (B%C))%C;
const result3 = (A*B)%C ;
const result4 = ((A%C)*(B%C))%C ;

console.log(`${result1}\n${result2}\n${result3}\n${result4}`);
