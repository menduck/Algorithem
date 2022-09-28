const input = 17; 

let arr = [];
for(let i =1;i<=input;i++){
  if(input%i === 0){
    arr.push(i)
  }
}


if(arr.length === 2){
  console.log("YES")
} else if (input === 0 || input === 1){
  console.log("NO")
} else {
  console.log("NO")
}