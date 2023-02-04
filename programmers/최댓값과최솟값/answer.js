const s = "1 2 3 4"
function solution(s) {
  let num = s.split(' ').map(v=>parseInt(v));
  console.log(num)
  let min = Math.min(...num);
  let max = Math.max(...num);
  let answer = `${min} ${max}`;
  return answer
}

console.log(solution(s))