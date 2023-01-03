const fs = require('fs');
const inputData = fs
    .readFileSync(0,'utf8')
    .toString()
    .trim()
    .split('\n')
    .map((i) => parseInt(i))

const remainder = inputData.map((x) => x%42)

const uniqueremainder = new Set(remainder);

const uniqueremainderLength = [...uniqueremainder].length
console.log(uniqueremainderLength)