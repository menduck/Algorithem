const input = "10 2";
const newinput = input.split(" ").map(v => parseInt(v))
const a = newinput[0], b= newinput[1];
const division = a/b, diviser = a%b
console.log(division,diviser)