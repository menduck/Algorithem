/**
 * 문제 접근
 * 각 number는 + 또는 -로 연산되어진다.
 * 연산이 가능한 모든 조합을 생성하기 위해 DFS를 활용한다.
 * numbers 배열의 각 숫자에 대해 두 개의 경우를 생성한다. 하나의 경우는 숫자를 추가(+)하고 다른 하나의 경우는 뺀다(-)
 * 이진 트리를 생성되고, 각 노드는 숫자를 더하고 빼는 고유한 조합을 나타낸다.
 */


function solution(numbers, target) {
  let count = 0;
  function dfs(depth,sum){
    if(depth < numbers.length){
      dfs(depth +1, sum + numbers[depth]);
      dfs(depth +1, sum - numbers[depth]);
    } else {
      if (sum === target){
        count++;
      }
    }
  }
  dfs(0,0);
  return count;
}

solution([4,1,2,1],4)

/**
 * # 시간복잡도
 * n이 배열의 길이일때, 시간 복잡도는 O(2^n)으로 연산되어진다.
 * dfs함수가 재귀적으로 자신을 두 번 호출하여 재귀 트리의 각 기준에 두 개씩 dfs를 생성하기 때문이다.
 * 
 * # BFS가 아니라 DFS를 선택한 이유?
 * 이 문제는 numbers 배열의 요소간의 연산을 통해 target값과 일치하는 모든 조합의 개수를 찾는 문제이다.
 * DFS는 가능한 모든 경로를 탐색하는데 적합하다. 반면에 BFS는 두 노드 사이의 최단 거리를 찾는데 더 적합하기 때문에 이 문제는 DFS가 더 효율적이다.
 */