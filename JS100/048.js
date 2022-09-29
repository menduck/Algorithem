const input = "AAABBBcccddd";
const inputArr = input.split('');

let answerArr = ''
for(let i =0;i<inputArr.length;i++){
  if(inputArr[i] === inputArr[i].toUpperCase()){
    answerArr += inputArr[i].toLowerCase()
  } else{
    answerArr += inputArr[i].toUpperCase()
  }
  
} console.log(answerArr)