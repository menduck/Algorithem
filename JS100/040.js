const input = "50\n5\n10\n10\n10\n20\n20";
const inputData = input.split('\n').map(v=>parseInt(v))
const limit = inputData[0]; //제한 무게


let limitedNum = []; // 탈 수 있는 인원수를 나열한다.
let sum = 0;
for(let i =2;i<inputData.length;i++){
  if(sum<=limit){
  sum += inputData[i];
  limitedNum.push(i-2); 
  } 
}
console.log(limitedNum[limitedNum.length-1])
