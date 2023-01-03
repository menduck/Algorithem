const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().trim().split('\n')
const data = inputData[1].split(' ');

const max = Math.max(...data);
const min = Math.min(...data);
console.log(`${min} ${max}`);


