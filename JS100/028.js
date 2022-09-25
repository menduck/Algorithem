const input ="Javascript";
const newInput = Array.from(input)
let answer = ''
for(let i =0;i<newInput.length-1;i++){
  let sumString = newInput[i]+' '+newInput[i+1]+'\n'
  answer += sumString
}
console.log(answer)