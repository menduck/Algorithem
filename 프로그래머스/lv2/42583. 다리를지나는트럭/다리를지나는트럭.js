// solution 
/*
- 문제 접근
시간 | 다리를 지난 트럭 | 다리를 건너는 트럭 | 대기 트럭
0 | [] | [0,0] | [7,4,5,6]
1 | [] | [0,7] | [4,5,6]
2 | [] | [7,0] | [4,5,6]
3 | [7] | [0,4] | [5,6]
4 | [7] | [4,5] | [6]
5 | [7,4] | [5,0] | [6]
6 | [7,4,5] | [0,6] | []
7 | [7,4,5] | [6,0] | []
8 | [7,4,5,6] | [0,0] | []
*/

function solution(bridge_length, weight, truck_weights){
  crossingTruck = Array.from({length: bridge_length}).fill(0)
  // 다리를 건너는 트럭들의 무게 합
  let bridge_sum = 0;
  let seconds = 0;
  
  // 1초 시작
  seconds++
  crossingTruck.shift();
  bridge_sum += truck_weights[0]
  crossingTruck.push(truck_weights.shift())
  
  while(bridge_sum > 0){
    seconds++
    bridge_sum -= crossingTruck.shift()
    if((bridge_sum + truck_weights[0]) <= weight && truck_weights.length > 0){
      bridge_sum += truck_weights[0]
      crossingTruck.push(truck_weights.shift())
    } else {
      crossingTruck.push(0)
    }
  } return seconds
}

  
console.log(solution(2, 10, [7, 4, 5, 6]));
// solution - 실패
/**
  # 실패이유
  - 한 번에 다리에 탈 수 있는 무게를 기준으로 이중배열로 만듦
  - 하지만 truck_weights = [7,4,5,5,6]일때, 4인 트럭과 5인트럭이 한 다리에서 움직이고, 4인 트럭이 도착 후 5인 트럭과 5인트럭이 한 다리에 있는 경우를 놓침.
 */

// function solution(bridge_length, weight, truck_weights) {
//   // 최대 weigth인 부분합 배열 예) [[7],[4,5],[6]]
//   const maxWeightArr = truck_weights.reduce((result, num) => {
//     const currentSum = result[result.length - 1].reduce(
//       (acc, cur) => acc + cur,
//       0
//     );

//     if (currentSum + num <= weight) {
//       result[result.length - 1].push(num);
//     } else {
//       result.push([num]);
//     }

//     return result;
//   }, [[]]);

//   const secondsUnit =  maxWeightArr.map((v) => {
//     return (v.length * bridge_length) - (v.length -1)
//   })

//   return secondsUnit.reduce((acc, cur) => acc+cur,0) + 1
// }