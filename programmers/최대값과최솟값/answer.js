
function solution(s) {
  let num = s.split(' ').map(v=>parseInt(v));
  let min = Math.min(...num);
  let max = Math.max(...num);
  let answer = `${min} ${max}`;
  return answer
}