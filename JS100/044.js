const input = 18264;
const inputData = input.toString().split("").map(v=>parseInt(v))

let sum = 0;
for(let i = 0;i<inputData.length;i++){
  sum += inputData[i]
}

console.log(sum)