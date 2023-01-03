const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split('\n')

// inputData = ['10 5','1 10 4 9 2 3 8 5 7 6'];

const A = inputData[0].split(' ');
const data = inputData[1].split(' ');

// const n = parseInt(A[0]);
const x = parseInt(A[1]);



const result = data.reduce((acc,cur) => {
    if((cur < x)){
        return acc =[...acc,cur]
    }
    return acc
},[]);


console.log(result.join(' '))


