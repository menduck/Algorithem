const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString();
const Num = parseInt(inputData);
let sum = 0
for(let i = 0; i < Num+1;i++){
    sum += i
}
console.log(sum)