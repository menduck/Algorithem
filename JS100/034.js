const input = "176 156 155 165 166 169"
console.log(input.split(' ').join(' '))

const sortedInput = input.split(' ').sort((a,b)=> a-b).join(' ')

if(input === sortedInput){
  console.log("YES")
} else
console.log("NO")