const fs = require('fs');
const inputData = fs
    .readFileSync(0,'utf8')
    .toString()
    .trim()
    .split('\n')
    .map((i) => parseInt(i))
    
const inputDataMax = Math.max(...inputData);
const maxIndex = inputData.indexOf(inputDataMax)+1;


console.log(`${inputDataMax}\n${maxIndex}`);