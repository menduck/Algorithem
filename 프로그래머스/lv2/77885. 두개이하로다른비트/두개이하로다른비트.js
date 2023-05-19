
/**
  - x가 짝수 / 홀수인 경우를 따로 생각해야한다.
  1. x가 짝수인 경우 (100(2))
    - x의 2진수 마지막 숫자는 반드시 0이다. 그래서 비트 하나만 다른 수를 찾으려면 마지막 숫자를 1로 바꾼 수를 사용하면 된다. (예: 101(2))  이 수는 x+1의 2진수이다.
  2. x가 홀수인 경우
    2-1. x의 2진수 중 0이 포함된 경우 
      - 예를 들어, 101(2)인 경우, 이진수에서 뒤에서부터 첫 번째 0의 위치를 찾고, 그 위치에 있는 비트를 1로 변경하고 그 다음 위치의 비트를 0으로 변경한다. (예: 110(2))
    2-2. x의 2진수 중 0이 포함되지 않은 경우 
      - 11(2) 이면, 그 다음 젤 앞에 1을 10으로 바꿔준다.
      - 왜냐면, 다음 큰 이진수로 넘어가기 위해 1를 추가하여 비트를 증가시켜야함.

    - 참고
      - 비트연산자를 통해 비트가 다를 경우를 구하는 방법이 있었는데 비트연산자는 32비트 이상이면 32비트 정수로 변환되기 때문에 큰 수에는 적용하기 어려움
 */

// 최종 코드 - 성공
function solution(numbers) {
  return numbers.map((v) => f(v))

}

function f(x) {
  // 짝수
  if (x % 2 ===0){
    return x + 1 
  // 홀수
  } else {
    const binary = x.toString(2).split('')
    const zeroIdx =  binary.lastIndexOf('0');
    // 0이 있는 경우
    if (zeroIdx !== -1) {
      binary[zeroIdx] = 1
      binary[zeroIdx+1] = 0
      return parseInt(binary.join(''),2)
    // 0이 없는 경우
    } else {
      return parseInt([1, 0, ...binary.slice(1)].join(''),2)
    }
  }
}


// solution - 시간 초과
function solution(numbers) {
  const result = []
  numbers.forEach( num=> 
    result.push(getBitCount(num))
  )
  return result
}

// x보다 크고 x와 비트가 1~2개 다른 수들 중 제일 작은 수를 반환하는 함수
function getBitCount(number) {
  const binary = number.toString(2)
  
  while(true){
    number += 1
    const targetNumber = number.toString(2)
    const binaryArray = binary.padStart(targetNumber.length,'0').split('')
    const targetNumberArray = targetNumber.padStart(targetNumber.length,'0').split('')
    let count = binaryArray.filter((v,i) => v !== targetNumberArray[i]).length
    if ([1,2].includes(count)) {
      return number
    } 
  }
}

console.log(solution([5,7]))
