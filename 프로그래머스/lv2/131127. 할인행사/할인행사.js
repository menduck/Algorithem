```
# 문제 접근
- 10씩 제품을 array에 담는다
- 원하는 제품 하나씩 array에 원하는 개수만큼 들어있는지 확인한다.
  - filter로 원하는 제품을 추리고 개수를 구한 다음 원하는 개수인지 확인한다.
```

function solution(want, number, discount) {
  let count = 0
  for(let i = 0; i<= discount.length-10;i++){
    const ten_discount = discount.slice(i, i+10)
    let tmp = 0
    for(let j = 0; j < want.length; j++){
      if (ten_discount.filter(product => product === want[j] ).length === number[j]){
        tmp++
      } else {break}
    }
    if (tmp === want.length) count++
  }
  return count
}
console.log(solution(	["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
