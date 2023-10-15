/**
 * 접근방법
 * - bfs 사용하여 조건에 맞는 값을 누적합하여 arr에 담아 반환함.
 */

function solution(maps) {
  const row = maps.length;
  const col = maps[0].length;
  const graph = maps.map(v => v.split(''))
  const result = []
  
  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (graph[i][j] !== 'X') {
        result.push(dfs(i,j,graph,col,row))
      }
    }
  }

  return result.length ? result.sort((a,b) => a-b) : [-1] 
}

function dfs(x, y, graph, col, row) {
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];
  let sumDays = parseInt(graph[x][y]);

  graph[x][y] = 'X';
  const arr = [];
  arr.push([x, y]);

  while (arr.length > 0) {
    [x, y] = arr.pop();

    for (let i = 0; i < dx.length; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      if (0 <= nx && nx < row && 0 <= ny && ny < col && graph[nx][ny] !== 'X') {
        arr.push([nx, ny]);
        sumDays += parseInt(graph[nx][ny]);
        graph[nx][ny] = 'X';
      }
    }
  }
  return sumDays;
}

solution(['X123X', 'X4X5X', 'X678X', '9XXX1']);
