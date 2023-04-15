// 현재 위치에 있을때 전 행에서 가질 수 있는 가장 최댓값을 가진다.

function solution(land) {
  let sum = 0;

  for (let i = 1; i < land.length; i++) {
    for (let j = 0; j < land[i].length; j++) {

        let arr = land[i - 1].slice();
        arr[j] = 0;
        land[i][j] += Math.max(...arr);
        sum = Math.max(land[i][j], sum);
    }
  }
  return sum;
}

console.log(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]))


// solution - 실패
/*
- land의 첫 번째 행을 기준, 각 열의 원소 하나씩 경우의 수를 잡는다.
- 누적합의 최댓값이 나오는 열을 택하면서 다음 행으로 넘어간다.
- 여기서 indexOf로 최댓값 열을 찾기 때문에 누적합의 최댓값이 여러 경우일 경우 첫 번째 요소만 확인하기 때문에 실패함

// 예시
solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]) 기댓값 20 결과값 19
- 첫번째 행 중 첫번째 요소인 4 경우의 수를 보면
4*
=======
0 6* 6 5
=======
12* 0 12 10
=======
0 19* 18 17

결과값이 19가 나옴
*/

function solution2(land) {
  let maxScore = 0;
  for (let i = 0; i < land[0].length; i++) {
    maxScore = Math.max(score(land[0][i], i, land.slice(1)), maxScore);
  }
  return maxScore;
}

function score(x, index, numbers) {
  let num = x;
  let numIndex = index;
  for (number of numbers) {
    let sumNumber = number.map((v, i) => {
      if (i !== numIndex) {
        return v + num;
      } else return 0;
    });
    num = Math.max(...sumNumber);
    numIndex = sumNumber.indexOf(num);
  }
  return num;
}

// solution - 실패
// 1. 같은 열을 연속!해서 밟을 수 없다. 연속하지 않으면 밟을 수 있다.
// 2. 누적값이 2개 이상일때, indexOf는 젤 처음 찾은 인덱스를 반환해주기때문에 다른 경우의 수를 놓친다.
// function solution1(land) {
//   let maxScore = 0
//   for(let i = 0; i<4; i++){
//     maxScore = Math.max(score(land[0][i],i,land.slice(1)),maxScore)
//   }
//   return maxScore
// }

// function score(x,index,numbers){
//   let num = x
//   let numIndex = [index]
//   for(number of numbers){
//     let sumNumber = number.map((v,i) => {
//       if (!numIndex.includes(i)){
//         return v+num
//       } else return 0
//     })
//     num = Math.max(...sumNumber)
//     numIndex.push(sumNumber.indexOf(num))
//   }
//   return num
// }
// score(5,3,[[5,6,7,8],[4,3,2,1]])

// console.log(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
// console.log(solution([[0,1,1,10],[0,1,1,100]]))
// console.log(solution([[1, 1, 1, 2], [1, 1, 2, 1], [1, 2, 1, 1]]))
// console.log(solution([[6, 5, 5, 5], [3, 4, 3, 3], [3, 2, 2, 2]]))
// console.log(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
// console.log(solution([[5, 5, 5, 5]]))
// console.log(
//   solution([
//     [4, 3, 2, 1],
//     [2, 2, 2, 1],
//     [6, 6, 6, 4],
//     [8, 7, 6, 5],
//   ])
// );
