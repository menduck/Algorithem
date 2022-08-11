const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");

let ABC = [parseInt(inputData[0]),parseInt(inputData[1]),parseInt(inputData[2])];
ABC.sort();


const A = ABC[0];
const B = ABC[1];
const C = ABC[2];

if (A == B && B ==C){
    result1 = 10000+A*1000
    console.log(result1);
} else if (A===B || B ===C ){
    if (A ===B){
        console.log(1000+A*100);
    } else if( B ===C ){
        console.log(1000+B*100);
    }
} else if(A !== B && B !== C){
    console.log(C*100);
}
