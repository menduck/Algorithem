
function solution(dirs) {
  const direction = { U: [0, 1], D: [0, -1], L: [-1, 0], R: [1, 0] };

  
  let route = new Set();
  let [x,y] = [0,0];
  for (keyword of dirs) {
    // 현재 위치에서 움직였을때 위치
    let nx = x + direction[keyword][0]
    let ny = y + direction[keyword][1]

    if (-5<=nx && nx<=5 && -5<=ny && ny<=5){ // 범위 안에 있으면
      route.add("" + x+y+nx+ny) // 현재 위치와 움직인 위치를 문자열로 set에 넣어줌
      route.add("" + nx+ny+x+y) // 반대 방향도 넣어줌 (중복방지)

      // 현재 위치는 움직인 위치가 됨.
      x = nx
      y = ny
    }
  }
  return route.size / 2
}
// // solution - 실패
// // [0,0]에서 상좌하우(한바퀴)를 돌면 이동거리가 4가 나와야 되는데 3이 나옴.

// function solution1(dirs) {
//   const direction = { U: [0, 1], D: [0, -1], L: [-1, 0], R: [1, 0] };

//   let count = 0;
//   let point = [[0, 0]];
//   for (keyword of dirs) {
//     let nx = point.at(-1)[0] + direction[keyword][0]
//     let ny = point.at(-1)[1] + direction[keyword][1]

//     if (-5<=nx && nx<=5 && -5<=ny && ny<=5){
//       if(!point.map(item => item.toString()).includes([nx,ny].toString())){ // 한번도 가지 않은 길
//         count += 1
//       }
//       point.push([nx,ny])
//     }
//   }
//   return count
// }
console.log(solution("ULURRDLLU"));
// // console.log(solution1("ULDR"));
console.log(solution("LULLLLLLU"));

