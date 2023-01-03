const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(' '); // 문자열로 반환
const A = parseInt(inputData[0]); //숫자로 형변환 시킴
const B = parseInt(inputData[1]);

console.log(A+B);
console.log(A-B);
console.log(A*B);
console.log(Math.floor(A/B));
console.log(A%B);