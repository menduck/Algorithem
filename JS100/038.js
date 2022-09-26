const input = "97 86 75 66 55 97 85 97 97 95";
const sortedInput = input.split(' ').sort((a,b)=>b-a);
console.log(Math.max(...sortedInput))