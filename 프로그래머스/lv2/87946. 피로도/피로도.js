/*
# 문제 접근
- 초반엔 그리드
- DFS로 모든 조합을 찾아 max인 횟수를 반환한다.

*/
function solution(k, dungeons) {
  const dungeonsCount = dungeons.length
  const checked = new Array(dungeonsCount).fill(false) 
  let userGameCount = 0
  function dfs(k,curCnt){
    userGameCount = Math.max(curCnt, userGameCount)
    if (userGameCount === dungeonsCount){return userGameCount;}
    
    for(let i =0; i<dungeonsCount;i++){
      const [req,use] = dungeons[i]

      if (k >= req && !checked[i]) {
        checked[i] = true
        dfs(k-use, curCnt+1)
        checked[i] = false
      }
    }

  }
  dfs(k,0);
  return userGameCount;
}

solution(80,[[80,20],[50,40],[30,10]])

// solution2 - 최종코드
function solution(k, dungeons) {
  const dungeonsCount = dungeons.length
  const checked = new Array(dungeonsCount).fill(false)
  let userGameCount = 0
  function dfs(k,curCnt){
    userGameCount = Math.max(curCnt, userGameCount)

    // 재귀를 돌다가 유저가 탐험할 수 있는 최대 던전의 수가 하루에 탐험할 수 있는 던전의 수와 같다면 바로 그 값을 반환한다.
    if (userGameCount === dungeonsCount){return userGameCount;}
    
    for(let i =0; i<dungeonsCount;i++){
      const [req,use] = dungeons[i]

      if (k >= req && !checked[i]) {
        checked[i] = true
        dfs(k-use, curCnt+1)
        checked[i] = false
      }
    }

  }
  dfs(k,0);
  return userGameCount;
}

solution(80,[[80,20],[50,40],[30,10]])