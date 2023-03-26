/*
# 문제 접근
- 1. p가 될 수 있는 숫자를 n을 k진수로 바뀐 수에서 뽑기
- 2. 뽑은 숫자가 소수인지 판단하고 개수 반환
  - 소수 판단하는 함수 만들기
*/

// solution 1 - 시간초과
function solution(n, k) {
  const newN = n.toString(k)
  pArray = (newN.split(0)).filter(v => v>1)
  let result = 0
  for (let p of pArray ){
    result += isPrimeNumber(p)
  }
  return result
}

// 소수 판단 함수
function isPrimeNumber(number) {
  if (number === 1) return 0
  for (let i = 2; i <= number-1;i++){
    // 1과 자기 자신의 수외의 숫자에서 나누어 떨어지면 소수가 아님.
    if (number%i===0) return 0
  }
  return 1
} 

// solution 2 - 성공

function solution(n, k) {
  const newN = n.toString(k)
  pArray = (newN.split(0)).filter(v => v>1)
  let result = 0
  for (let p of pArray ){
    result += isPrimeNumber(p)
  }
  return result
}

// 소수 판단 함수
function isPrimeNumber(number) {
  for (let i = 2; i <= Math.sqrt(number);i++){
    // 제곱근까지만 순회함
    if (number%i===0) return 0
  }
  return 1
} 

// solution 3 - 최종 코드

function solution(n, k) {
  const newN = n.toString(k)
  return (newN.split(0)).filter(v => isPrimeNumber(parseInt(v,10))).length
}

// 소수 판단 함수
function isPrimeNumber(number) {
  if (!number || number === 1) return false
  for (let i = 2; i <= Math.sqrt(number);i++){
    // 제곱근까지만 순회함
    if (number%i===0) return false
  }
  return true
}  

/*
# 시간 초과가 났던 이유
- 소수 판단하는 함수에 시간복잡도가 높았기 때문
- solution1에서 소수 판단하는 함수의 시간 복잡도는 O(n)이다. 
- solution2에서 소수 판단하는 함수의 시간 복잡도는 O(squrt(n))이다.
- 따라서 제곱근을 활용해 소수를 판단하는 함수가 불필요한 숫자가 반복되는 것을 방지함으로 n이 큰 값이 들어올땐 더 효율적이다.
*/



