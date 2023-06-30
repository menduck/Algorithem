/**
 *  처음 순서가 [1,2,3,4,5] -> 만들어야 되는 순서가 order 배열
 *  스택, 선입선출을 생각하면서 풂
 *  주의! 파이썬과 다르게 js에선 마지막 요소를 가져올때 at 메서드를 사용
 */
function solution(order) {
  // const beforeOrder = Array.from({length:order.length}, (v,i) => i+1)
  let beforeOrderNum = 1
  let result = 0
  const container = []
  while(beforeOrderNum < order.length +1){
    container.push(beforeOrderNum)
    while(container.length > 0 && container.at(-1) === order[result] ){
      container.pop()
      result++
    }
    beforeOrderNum++
  }

  return result
}