const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString() ;


let num = +inputData[0];



for(let i = 1 ; i < 10; i++){
    console.log(`${num} * ${i} = ${num*i}`);
}

