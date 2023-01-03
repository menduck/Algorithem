const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split("\n");
const times = inputData[0].split(" ");
const cookingTimes = parseInt(inputData[1]);
const H = parseInt(times[0]);
const M = parseInt(times[1]);


solution(H,M,cookingTimes);

function solution(H,M,cookingTimes){
    const result = H*60+M+cookingTimes ;
    const resultH = Math.floor(result/60);
    const resultM = result%60;
    if (resultH >= 24){
        console.log(resultH-24,resultM);
    }else
    console.log(resultH,resultM);

}
