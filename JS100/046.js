let str = '';
for(let i = 1;i<=20;i++){
  str += i
}

const newStr = str.split('');
let sum = 0;
for(let j = 0;j<newStr.length;j++){
  sum += parseInt(newStr[j])
}

console.log(sum)