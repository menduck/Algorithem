function solution(maps) {
  const dx = [1,0,-1,0];
  const dy = [0,1,0,-1];
  const [n,m] = [maps.length, maps[0].length]
  
  // 시작
  const queue = [[0,0,1]];
  
  while(queue.length){
    const [y,x, count] = queue.shift()
    if (x === m-1 && y === n-1){
      return count;
    }
    for(let i =0; i < 4; i++){
      const ny = y + dy[i]
      const nx = x + dx[i]

      if (nx >= 0 && nx < m && ny >= 0 && ny < n && maps[ny][nx]  === 1 ) {
          queue.push([ny,nx,count+1]);
          maps[ny][nx] = 0 ;
      }
    }
  }
  return -1;
}

// solution - 실패 / 시간초과
function solution(maps) {
  const dx = [1,0,-1,0];
  const dy = [0,1,0,-1];
  const [n,m] = [maps.length, maps[0].length]
  const visitedCount = Array.from({length:n},()=> Array(m).fill(1));
  
  // 시작
  const queue = [[0,0]];
  // 방문 체크
  visitedCount[0][0] = 1

  
  while(queue.length){
    const [y,x] = queue.shift()
    for(let i =0; i < 4; i++){
      const ny = y + dy[i]
      const nx = x + dx[i]

      if (nx >= 0 && nx < m && ny >= 0 && ny < n && maps[ny][nx]  === 1 && visitedCount[ny][nx] === 1) {
          queue.push([ny,nx]);
          visitedCount[ny][nx] = visitedCount[y][x] +1
      }
    }
  }

  return visitedCount[n-1][m-1] === 0  ? -1 : visitedCount[n-1][m-1]
}

solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])