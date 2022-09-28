const input = "hqllo my namq is hyqwon";

let arrInput = Array.from(input);

for(let i =0;i<arrInput.length;i++){
  if(arrInput[i] === "q"){
    arrInput[i] = "e"
  } else if (arrInput[i] === "Q"){
    arrInput[i] = "E"
  }
}

const answer = arrInput.join('')
console.log(answer)