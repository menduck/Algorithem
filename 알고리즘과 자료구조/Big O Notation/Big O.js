function addUpTo(n) {
  let sum =0;
  for(let i =1;i<=n;i++){
    sum += i
  }
  return sum
}

let t1 = performance.now(); // 브라우저가 이 문서를 만든 시간을 알려줌
addUpTo(1000000000); // 큰 숫자 입력
let t2 = performance.now(); // 앞 줄의 기능을 한 후 문서를 연 시간
console.log(`시간 경과는 ${(t2-t1)/1000} 초이다.`)