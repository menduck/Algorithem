// solution - 성공 / 다른 사람 코드

function solution(m, n, board) {
  board = board.map((v) => v.split(""));

  while (true) {
    let founded = [];

    // 2*2 체크
    for (let i = 1; i < m; i++) {
      for (let j = 1; j < n; j++) {
        if (
          board[i][j] &&
          board[i][j] === board[i][j - 1] &&
          board[i][j] === board[i - 1][j - 1] &&
          board[i][j] === board[i - 1][j]
        ) {
          founded.push([i, j]);
        }
      }
    }
    // 좌 상단에 있는 좌표 저장
    // board = ['A','A'],['A','A'] 이면 founded = [1,1]
    // founded = []

    if (!founded.length) return [].concat(...board).filter((v) => !v).length;
    
    // 2*2 모두 0으로 만듦
    founded.forEach((a) => {
      board[a[0]][a[1]] = 0;
      board[a[0]][a[1] - 1] = 0;
      board[a[0] - 1][a[1] - 1] = 0;
      board[a[0] - 1][a[1]] = 0;
    });

    // console.log(board)
    // borad 재정렬
    for (let i = m - 1; i > 0; i--) {
      // 열이 온전히 있으면 
      if (board[i].every(v => v)) continue;
      // if (! board[i].some(v => ! v)) continue;

      for (let j = 0; j < n; j++) {
          for (let k = i - 1; k >= 0 && ! board[i][j]; k--) {
              if (board[k][j]) {
                  board[i][j] = board[k][j];
                  board[k][j] = 0;
                  break;
              }
          }
      }
  }
  // console.log(board)
}
}

// console.log(solution(3, 3, ["RRF", "RRR", "TRR"]));
console.log(solution(3, 6, ["RRFACC", "RRRFCC", "TRRRAA"]));


// solution - 실패
// 1. board 재정렬 못함 2. 2*2 이 여러 개일때, 중복으로 개수를 셈

function count(m, n, x,y, board) {
  const dx = [0,1,1]
  const dy = [1,0,1]

  let block = 1

  for (let i = 0; i < 3 ; i++){
    const nx= x + dx[i]
    const ny= y + dy[i]

    if (nx >= 0 && ny >= 0 && nx < m && ny < n && board[nx][ny] === board[x][y])
    {
      // checked[nx][ny] = 1
      block++
      count(m,n,nx,ny,board)
      }
    else {
      // checked[nx][ny] = 0
      return 0
    }
  }
  // return checked.flat().reduce((acc,cur) => acc+cur,0)
  return block

}

function solution(m,n,board){
  let result = 0
  // let checked = Array.from({length:m},()=> Array(n).fill(0));
  for (let x = 0; x < m ; x++ ){
    for (let y = 0; y < n; y++){
        result += count(m,n,x,y,board)
    }
  }
  return result
}