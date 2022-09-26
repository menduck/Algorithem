const input = "원범 원범 혜원 혜원 원범 혜원 유진 혜원";
const arr = input.split(' ') //input을 배열로 만듦
const set = new Set(arr); //중복된 값만 추출
const setArr = Array.from(set) //set이 객체임으로 배열로 다시 바꿈

let countArr = [];

for(let i = 0; i<setArr.length;i++){
  let count = 0; //두 번째 for문이 끝나면 countArr에 값을 넣고 카운팅 개수 초기화
  for(let j =0; j<arr.length;j++){
    if(setArr[i] === arr[j]){ 
      count++
    }
  } countArr.push(count)
}
const countMax = Math.max(...countArr) //카운팅배열 중 가장 큰 값을 추출하고
const maxName = setArr[countArr.indexOf(countMax,0)] // 인덱스 값에 해당되는 값을 저장함.

console.log(`${maxName}(이)가 총 ${countMax}표로 반장이 되었습니다.`)