/*
  # solution - 실패/시간초과
  - topping의 길이가 최대 1,000,000이고, for문으로 모든 가능한 분할(slice의 시간 복잡도는 O(n)을 따지기 때문에 O(n2)임으로 시간 초과 발생
 */

function solution(topping) {
  let count = 0;
  for (let i = 0; i < topping.length; i++) {
    const me = new Set(topping.slice(0, i + 1));
    const you = new Set(topping.slice(i + 1));
    if (me.size === you.size) {
      count++;
    }
  }
  return count;
}


// solution - 성공
// map 객체로 각 토핑의 번호와 개수를 담아, 하나씩 비교해 준다. 
function solution(topping) {
  const map = new Map();
  const you = new Set();
  let count = 0;
  
  // 각 토핑의 개수를 담음 {토핑의 번호 => 그 토핑의 개수}
  for (let i = 0; i < topping.length; i++) {
    if (map.has(topping[i])) {
      map.set(topping[i], map.get(topping[i]) + 1);
    } else {
      map.set(topping[i], 1);
    }
  }

  for (let i = 0; i < topping.length; i++) {
    you.add(topping[i]);

    // 내꺼에서 토핑 한 개씩 준다.
    map.get(topping[i])-1 === 0
      ? map.delete(topping[i])
      : map.set(topping[i], map.get(topping[i]) - 1);

      // 토핑의 종류의 개수가 같으면 count 1개씩 증가
    if (you.size === map.size) count++;
  }
  return count;
}
