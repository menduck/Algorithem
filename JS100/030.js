const input = "pineapple is yummy"+"\n"+"apple";
const standard = input.split("\n")[0];
const hiddenStr =  input.split("\n")[1];

const answer = standard.indexOf(hiddenStr)
console.log(answer)