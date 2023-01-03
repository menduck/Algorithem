const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().trim().split(' ')

//onst inputData =[2,1,2,1,2,1]

const blackNum = [1,1,2,2,2,8]
let result = ''

for(i = 0; i < 6; i++){
    subtract = (parseInt(blackNum[i]) - parseInt(inputData[i]))
    result += subtract +' '
}

console.log(result)