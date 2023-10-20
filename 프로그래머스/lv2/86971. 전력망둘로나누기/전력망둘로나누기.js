/**
 * 접근 방법
 * 1. 트리를 만든다.
 * 2. 노드 하나씩 방문한다.
 * 2-1. 끊어질 노드를 방문 표시를 한다.
 * 2-2. bfs로 방문할 노드들의 개수를 구한다.
 * 3. 차이는 (총 노드의 개수 - 방문한 노드 개수) - 방문한 노드 개수의 절대값이다.
 *  - n=9, 첫번째 노드가 연결된 개수 = 8일 경우 두 전력망이 가진 노드의 개수 차이는 7이다.
 * 4. 차이를 계산한 배열 중 가장 최솟값을 반환한다.
 */

function solution(n, wires) {
  const result = [];
  //트리 만들기
  const tree = Array.from(Array(n + 1), () => []);

  wires.map((element) => {
    let [a, b] = element;
    tree[a].push(b);
    tree[b].push(a);
  });

  let answer = 0;
  tree.forEach((eles, i) => {
    eles.forEach((v) => {
      const visited = Array.from(Array(n + 1), () => false);
      visited[v] = true;
      result.push(getBfsCount(i, visited, tree));
    });
  });
  const DiffArr = result.map((v) => Math.abs(n - v - v));

  return Math.min(...DiffArr);
}

// 노드와 연결된 노드 개수를 반환함
function getBfsCount(start, visited, tree) {
  const q = [start];
  let cnt = 0;
  while (q.length !== 0) {
    const current = q.shift();
    visited[current] = true;
    tree[current].forEach((v) => {
      if (!visited[v]) {
        q.push(v);
      }
    });
    cnt++;
  }
  return cnt;
}
solution(9, [
  [1, 3],
  [2, 3],
  [3, 4],
  [4, 5],
  [4, 6],
  [4, 7],
  [7, 8],
  [7, 9],
]);
