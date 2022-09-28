
function solution(a,b){
  const week = ['일', '월', '화', '수', '목', '금', '토'];
  console.log(week[new Date(2020,a-1,b).getDay()]) 
}
solution(9,28)


// month은 1월이 0으로 계산되므로 a-1