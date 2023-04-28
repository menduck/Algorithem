
// solution - stack으로 풀어야함 => O(n)
// stack에 index를 쌓으면서 가장 가까운 큰 수를 찾으면 pop을 하여 해당 index에 가장 가까운 큰 수를 저장한다. 

function solution(numbers) {
  const answer = Array(numbers.length).fill(-1);
  const stack = [];
  for (let i = 0; i < numbers.length; i++) {
    console.log(i,stack)
    while (stack && numbers[stack.at(-1)] < numbers[i]) {
      answer[stack.pop()] = numbers[i];
    }

    stack.push(i);
  }
  return answer;
}

// 시간초과 O(n^2)
function solution1(numbers) {
  const result = []
  for(let i = 0; i< numbers.length; i++){
    const maxArray = numbers.slice(i+1).filter((num) => numbers[i] < num)[0]
    result.push(maxArray ? maxArray : -1)
  } return result
}

solution([9, 1, 5, 3, 6, 2])