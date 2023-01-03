const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString()
const n = parseInt(inputData)

// const n = 5;
//  const strings = ['*','**','***','****','*****']

result = '';

for(let i = 1 ; i < n+1 ; i++){
    for(let j = 1 ; j <= i;j++){
        result += '*'; // 순회하면서 '*'이 누적된다.
    }  
                       
    result += "\n"   //한 줄씩 엔터값을 준다 
}

let arr = result.split('\n')
arr = arr.slice(0,-1);

const longestLength = arr.map(value => value.length)[n-1];

arr.forEach(value => console.log(value.padStart(longestLength)));