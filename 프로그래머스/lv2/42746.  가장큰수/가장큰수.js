/**
  # solution - 성공
  - 다중 정렬
    - 이중array를 만들고, 1. 첫 번째 자리가 큰 순서대로 정렬
    - 2. 첫 번째 자리가 같은 경우, 숫자를 합쳐서 비교하는 방식으로 숫자를 정렬
 */

function solution(numbers) {
  if (numbers.every((v) => v === 0)) return '0';

  const splitedNumbers = numbers.map((v) => v.toString().split(''));
  return splitedNumbers
    .sort((a, b) => {
      const numA = a[0];
      const numB = b[0];

      if (numA > numB) return -1;
      if (numA < numB) return 1;

      const newA = a.join('') + b.join('');
      const newB = b.join('') + a.join('');
      if (newA > newB) return -1;
      if (newA < newB) return 1;
    })
    .flat()
    .join('');
}

console.log(solution([3, 30, 34]));

// solution - 코드 개선
// 문자열은 슬라이싱이 되므로 굳이 array형태로 안 만들어도 됨.

function solution(numbers) {
  if (numbers.every((v) => v === 0)) return '0';

  // 문자열은 슬라이싱이 됨
  const splitedNumbers = numbers.map((v) => v.toString());
  return splitedNumbers
    .sort((a, b) => {
      const numA = a[0];
      const numB = b[0];

      if (numA > numB) return -1;
      if (numA < numB) return 1;

      const newA = a + b;
      const newB = b + a;
      if (newA > newB) return -1;
      if (newA < newB) return 1;
    })
    .join('');
}

// solution - 추가 풀이
// numbers의 원소는 0 이상 1,000 이하 => numbers의 원소를 최대 천자리를 만든다.(ex) 1 => 111) 그 다음 크기를 비교해서 정렬한다.
function solution(numbers) {
  if (numbers.every((v) => v === 0)) return '0';
  const splitedNumbers = numbers.map((v) => v.toString());
  return splitedNumbers
    .sort((a, b) => {
      const newA = a.repeat(3);
      const newB = b.repeat(3);

      if (newA > newB) return -1;
      if (newA < newB) return 1;
    })
    .join('');
}
