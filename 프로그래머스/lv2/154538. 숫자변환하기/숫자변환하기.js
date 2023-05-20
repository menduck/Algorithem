// solution 성공

/*
# 문제접근
- 1. bfs방식으로 접근
- 2. 하향식 방법
  - 상향식으로 접근하는 경우 모두 정수이기때문에 모든 경우의 수를 따져봐야 한다.
  - 하지만 하향식으로 접근하면, 실수인 경우는 제외하고 경우의 수를 따지기 때문에 조금 더 빨리 답을 찾을 수 있다.

# 추가적으로 생각해야할 것.
  - js는 queue 자료 구조를 기본적으로 제공하지 않기 때문에, 
  - shift() 메서드를 실행하는 과정에서 다른 모든 요소들을 한 칸씩 앞으로 이동시켜야 하므로, 시간 복잡도가 O(n)이다. 
  - 그래서 시간 성능면을 고려해야 한다.
 */

function solution(x, y, n) {
  // 테스트 코드 6번
  // x===y인 경우도 따져야 함.
  if (x===y){
    return 0
  }
  const que = [];
  let count = 1
  que.push([y,count]);
  while(que.length >0){
    const num = que.shift();
    const result = [num[0] - n, num[0]/2, num[0]/3 ]
    if (result.includes(x)){
      return num[1]
    } else {
      result.filter((v) => v > 0 && v % 1 === 0).forEach((v) => que.push([v,num[1]+1]))
    }
  }
  return -1
}

// 추가 풀이 (dp)
// - 중복 계산을 피하고 이미 계산된 값을 활용하기 때문에 연산의 반복을 줄일 수 있음.

function solution(x, y, n) {
  if (x === y) return 0;
  const dp = {};
  dp[x] = 0;
  let data = [x];
  while (data.length) {
    const newData = [];
    for (const d of data) {
      for (const e of [d + n, d * 2, d * 3]) {
        // 이미 계산된 값이 있는지 확인하고, 있으면 다음 반복문으로 넘어가기 때문에, 연산 횟수를 효율적으로 계산함.
        if (e > y || dp[e]) continue;
        if (e === y) return dp[d] + 1;
        dp[e] = dp[d] + 1;
        newData.push(e);
      }
    }
    data = newData;
  }
  return -1;
}

console.log(solution(10, 40, 5))