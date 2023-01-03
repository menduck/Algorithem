const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

const totalM = (A*60+B)-45;

if (totalM >0){
const resultA = Math.floor(totalM / 60);
const resultB = totalM % 60 ;
console.log(resultA, resultB);

} else if (totalM < 0 ){
const totalM1 = 1440 + totalM;
const resultAA =  Math.floor(totalM1 / 60);
const resultBB = totalM1 % 60;
console.log(resultAA, resultBB);

} else if (totalM === 0){
    console.log("0 0");
}
