const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString()
const N = parseInt(inputData)

result = ''

for(let i = 1 ; i < N+1 ; i++){
    result += '*'
    console.log(result)
}
