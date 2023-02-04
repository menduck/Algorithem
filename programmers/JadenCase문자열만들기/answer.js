const input = "3people unFollowed     me";
//모든 문자를 소문자로 바꿔줌.
let strInput = input.toLowerCase().split(' ')

let answer =[];
for(let i =0;i<strInput.length;i++){
  // 배열 안에 있는 문자들을 분리시켜 앞 문자를 가져옴.
  let splitedStr = strInput[i].split('');
  ;
  // 예외처리 - 공백
  if(splitedStr[0] != undefined){
    splitedStr[0] = splitedStr[0].toUpperCase()
  }
  answer.push(splitedStr.join(''));
  
  
} 
console.log(answer.join(' '))

