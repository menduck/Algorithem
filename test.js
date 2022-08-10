/*const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");

const H = parseInt(inputData[0]);
const M = parseInt(inputData[1]);*/

const H = 10;
const M = 10;

solution(H,M);

function solution(H,M){
    if(M>=45){
        console.log(H,M-45);
    } else if(M<45){
        if (H !==0){
            console.log(H-1,60+M-45);
        } else if( H === 0){
            console.log(23, 60+M-45);
        }
    }
}
