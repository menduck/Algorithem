const input = "2 5"
const newInput = input.split(' ').map(v => parseInt(v))
const a = newInput[0], b=newInput[1]
console.log(Math.pow(a,b))