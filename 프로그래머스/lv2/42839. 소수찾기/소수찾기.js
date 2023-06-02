// 소수 판별 함수
function isPrimeNumber(number) {
  if (number <= 1) return false;
  if (number % 2 === 0) return number === 2 ? true : false;

  const sqrt = parseInt(Math.sqrt(number));
  for (let i = 3; i <= sqrt; i += 2) {
    if (number % i === 0) return false;
  }
  return true;
}

// 순열
function solution(numbers) {
  const splitedNumbers = numbers.split('');
  const result = new Set();
  function permutation(permu, rests, result) {
    rests.forEach((v, idx) => {
      const rest = [...rests.slice(0, idx), ...rests.slice(idx + 1)];
      permutation([...permu, v], rest, result);
    });
    if (rests.length<splitedNumbers.length) return result.add(parseInt(permu.join(''),10));
  };
  permutation([], splitedNumbers, result);
  return Array.from(result).filter((v) => isPrimeNumber(v)).length
}

console.log(solution('123'));
