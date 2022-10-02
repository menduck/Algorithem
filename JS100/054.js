const input= "1 2 3 4 5";

const inputData = input.split(' ').map(v => parseInt(v));


const answer = []
for(let i = inputData[0];i<=inputData.length;i++){
  answer.push(i)
}

//1. 배열을 비교하는 방법(문자열로 비교)
if(answer.join('') === inputData.join('')){
  console.log("YES");
} else {
  console.log("NO") }

  //배열 안에 여러가지 타입이 있을 경우 문제가 발생한다.

//2. JSON.stringify : json, Object 객체를 문자열로 변환, JSON.parse : 문자열을 json, Object로 변환

if(JSON.stringify(answer) === JSON.stringify(inputData)){
  console.log("YES")
} else {
  console.log("NO")
}


