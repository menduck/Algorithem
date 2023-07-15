/**
 * 문제 풀이
 * - 세 가지 방향이 있음(위 -> 아래, 왼 -> 오, 아래 -> 위)
 *    - 위 -> 아래 [x++, 고정]
 *    - 왼 -> 오 [고정, y++]
 *    - 아래 -> 위 [x--, y++]
 */
function solution(n) {
  const numberArr = Array.from({ length: n }, (_, i) =>
    new Array(i + 1).fill(0)
  );
  let x = -1;
  let y = 0;
  let num = 1;
  while (n > 0) {
    // 위 -> 아래
    for (let i = 0; i < n; i++) {
      numberArr[++x][y] = num++;
    }
    // 왼 -> 오
    for (let i = 0; i < n - 1; i++) {
      numberArr[x][1 + y++] = num++;
    }
    // 아래 -> 위
    for (let i = 0; i < n - 2; i++) {
      numberArr[x-- - 1][y-- - 1] = num++;
    }

    n -= 3;
  }
  return numberArr.flat();
}

solution(4);
// solution(5);
