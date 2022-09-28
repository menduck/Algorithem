const input = "97 86 75 66 55 97 85 97 97 95";
const sortedInput = input.split(' ').sort((a,b)=>b-a);
console.log(sortedInput)

//3번째로 큰 수 찾기

const set = new Set(sortedInput)
const third = Array.from(set)[2];

//1~3위 학생들의 수
let count = 0
for(let i =0;i<sortedInput.length;i++){
  if(third <= sortedInput[i]) count++

}

console.log(count)