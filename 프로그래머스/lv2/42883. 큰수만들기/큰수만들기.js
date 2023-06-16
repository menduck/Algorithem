function solution(number, k) {
  let numberArr = number.split('').map(v => parseInt(v,10))
  let targetNumber =  number.length - k;
  const answer = [];
  
  while(targetNumber > 0){
    let fristNum;
    if (targetNumber === 1){
      fristNum = numberArr[0]
    } else {
      fristNum = Math.max(...numberArr.slice(0,targetNumber-1))
      console.log(numberArr.slice(0,targetNumber-2))
    }
    answer.push(fristNum)
    const fristIdx = numberArr.indexOf(fristNum)
    numberArr = numberArr.slice(fristIdx+1)

    targetNumber--
  }
  console.log(answer)
  return answer.join('')
}

solution("4177252841", 4)
// solution("1924", 2)

// 다른 사람 풀이
function solution(number, k) {
  const answer = [];
  for (let num of number) {
    while (k > 0 && answer[answer.length - 1] < num) {
      answer.pop(num);
      k -= 1;
    }
    answer.push(num);
  }
  return answer.join("").slice(0, number.length - k);
}