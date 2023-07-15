/**
 * 문제 접근
 * 일의 자리 수가 1,2,4로 3번씩 반복됨.
 *  
 * n이 0이 될 때까지 반복한다.
 *  - 3으로 나누어 떨어지면 n은 몫에 -1을 해준다.(만약 n=3이면, 3으로 나눈 몫이 1이 되기 때문에 -1을 해주어 0으로 만듦)
 *    - 3으로 나누어 떨어지면 반환값 일의 자리 수는 '4'이다.
 *  - 3으로 나누어 떨어지지 않으면 n은 3으로 나눈 몫으로 재할당
 *    - 3으로 나누어 떨어지지 않으면 반환값은 3으로 나눈 나머지이다(1아니면 2)
 */
function solution(n) {
  let answer = ''
  while(n){
    if(n%3===0){
      answer+='4'
      n = Math.floor(n/3) -1
    }else{
      answer += String(n%3)
      n = Math.floor(n/3)
    }
  }
  return answer.split("").reverse().join("")
}

console.log(solution(3))