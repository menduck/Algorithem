const fs = require('fs');
const inputData = fs
    .readFileSync(0,'utf8')
    .toString()
    .trim()
    .split('\n')

// const inputData = ['4','1 100 100 100']
const caseN = parseInt(inputData[0])

const score = inputData[1].split(' ').map((i)=>parseInt(i))
const scoreMax = Math.max(...score);
const newScore = score.map((i)=>i/scoreMax*100)

const newScoreSum = newScore.reduce((a,b)=>a+b,0);
const average = newScoreSum/caseN
console.log(average)

