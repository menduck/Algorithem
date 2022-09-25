const input = "20 30 40"
const newInput = input.split(' ').map(v => parseInt(v))
const average =newInput.reduce((acc,cur)=>acc+cur)/newInput.length;
console.log(average)
