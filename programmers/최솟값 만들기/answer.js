const A = [1,2];
const B = [3,4];

function solution(A,B){
  const sortA = A.sort((a,b)=>a-b) // 오름차순
  const sortB = B.sort((a,b)=>b-a) // 내림차순
  sum = 0;
  for(let i =0;i<sortA.length;i++){
      sum += sortA[i]*sortB[i] // 누적해서 더해줌.

  } return sum
}
