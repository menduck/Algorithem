function solution(n, t, m, p) {
  // t * m 개수의 n진법 배열을 저장 (대략적으로 잡아서 나중에 t만큼 잘라서 반환함.)
  numRange = Array.from({length: t*m}, (v,i) => i.toString(n));
  // 숫자를 하나씩 array에 저장
  numbers = numRange.join('').split('');
  let answer = ''
  // i는 튜브의 순서 인덱스 번호
  for (let i = p-1; i< numbers.length; i += m){
    // 대문자로 변환, 숫자는 숫자로
    answer += numbers[i].toUpperCase();
  }
  return answer.slice(0,t);

}

solution(	2, 4, 2, 1)
console.log(solution(16, 16, 2, 1))


// 새롭게 배운점
// 0~n까지 숫자 범위 배열 생성하기

var arr1 = Array.from({
  length: 5 // Create 5 indexes with undefined values
},
function(v, k) { // Run a map function on said indexes using v(alue)[undefined] and k(ey)[0 to 4]
  return k; // Return k(ey) as value for this index
}
);
console.log(arr1);

// 출처 https://stackoverflow.com/questions/40528557/how-does-array-fromlength-5-v-i-i-work