# programmers 문제 풀이

# 2022.08.01
## level1 최대공약수와 최소공배수
### 문제
* 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
* 자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.

### solution
```javascript
function solution(a,b){
    return [gcd(a,b), lcm(a,b) ];
}

function gcd(a,b){
    const remainder = a%b;
    if (remainder === 0) return b;
    return gcd(b,remainder);
}
function lcm(a,b){
    return (a*b)/gcd(a,b) ;
}
```
###  다른 사람 코드
```javascript
function greatestCommonDivisor(a, b) {return b ? greatestCommonDivisor(b, a % b) : Math.abs(a);}
function leastCommonMultipleOfTwo(a, b) {return (a * b) / greatestCommonDivisor(a, b);}
function gcdlcm(a, b) {
    return [greatestCommonDivisor(a, b),leastCommonMultipleOfTwo(a, b)];
}
```
for문을 이용하여 해결
```javascript
function gcdlcm(a, b) {
    var r;
    for(var ab= a*b;r = a % b;a = b, b = r){}
    return [b, ab/b];
}
```
## level1 나머지가 1이 되는 수

```javascript
function solution(n) {
    let result = [];
    for(let i = 2; i<=n ; i++){ // 1제외한 약수 구하기
        if(n%i === 1){
            result.push(i)
        }
    }
    return result[0]
}
```
### 다른 풀이
```javascript
function solution(n, x = 1) {    
    while (x++) {
        if (n % x === 1) {
            return x;
        }
    }    
}
```
## level1 짝수와 홀수
### 풀이
```javascript
function solution(num) {
    if(num%2===0 || num ===0){
        return "Even"
    } else
        return "Odd"
}
```
- 함수명을 관련되게 적자.
### 다른 사람 풀이
```javascript
function evenOrOdd(num) {
  return num % 2 ? "Odd" : "Even";
}
```
>> 새롭게 안 사실
- 삼항 연산자를 사용해 풂.
- num % 2 === 0을 안해줘도 됨.
- 어차피 0은 false임으로 따로 if문으로 안빼도 됨.

## level 자릿수 더하기
### 풀이
```javascript
function solution(n){
    let splitedN = Array.from(String(n)); // n을 문자열로 바꾸고 array에 하나씩 둠
    let sum = 0;
    for(let i = 0; i < splitedN.length;i++){
        sum += parseInt(splitedN[i]) //i가 순회하면서 array의 요소들을 더함.
      }
    return sum
}
```
### 다른 사람 풀이
```javascript
function solution(n){
    // 쉬운방법
    return (n+"").split("").reduce((acc, curr) => acc + parseInt(curr), 0)
}
```
- (n+"").split("")
n을 나누고
- reduce((acc, curr) => acc + parseInt(curr), 0)
reduce를 이용해 더한다.
currentInex = 0 을 설정해줘야 배열1번째 부터 순회하면서 누적된다.

## level1 정수 제곱근 판별
### 풀이
- 처음 제출 했던 답
```javascript
const n = 11;
if(Math.sqrt(n)*Math.sqrt(n) === n){
    console.log(Math.pow((Math.sqrt(n)+1),2))
} else
    console.log(-1)
```
정수가 아닌 숫자를 제곱하면 정수가 나오지 않는 것을 조건을 달았다.
하지만 정수가 나오는 경우도 있다는 것을 깨닫고 (예를 들어 n =11이면 11의 제곱근을 곱하면 정수 11이 나옴.) 정수 판별식을 검색했다.

>> 정수 판별법
1. % 1
n%1 === 0 
정수를 1로 나누면 나머지는 반드시 0으로 나온다.

2. 내장매서드인 Number.isInteger()함수 이용
Number.isInteger(n) // n이 정수이면 true 정수가 아니면 false가 나온다.

- 최종 풀이
```javascript
function solution(n) {
    let sqrtN = Math.sqrt(n)
    if(sqrtN%1 === 0){
        return (sqrtN+1)*(sqrtN+1)
    } else
        return -1
}
```
## level1 약수의 합
### 풀이
```javascript
function solution(n) {
    let divisor = [];
    // 약수를 구하는 for문 
    for(let i = 1; i<=n;i++){
        if(n%i ===0){
            divisor.push(i)
        }
    }
    // divisor 요소들을 다 더함.
    let answer = divisor.reduce((acc,cur) => acc+ parseInt(cur),0)
    return answer
}
```

### 다른 사람 풀이
```javascript
function solution(num) {
    let sum = 0;
    for (let i = 1; i <= num; i++) {
        if (num % i === 0) sum += i
    }
    return sum
}
```
reduce를 사용하여 따로 더하는 변수를 생성하지 않아도 약수를 뽑아내면서 더하면 더 간단하게 코드를 짤 수 있다.

## level1 자연수 뒤집어 배열로 만들기
### 풀이
```javascript
function solution(n) {
    let arrN = Array.from(String(n),Number); // 숫자를 요소로 가진 배열을 만들어 준다.
    let answer = [];
    for(let i = arrN.length-1 ; i >= 0 ; i--){ // index를 하나씩 감소하여 배열에 push한다.
        answer.push(arrN[i])
    }
        return answer
}
```
### 다른 사람 풀이
1. 문자열로 풀기
```javascript
function solution(n){
    return (n+'').split('').reverse().map(v => parseInt(v));
}
```
n을 문자열로 나누고 reverse을 이용하여 배열을 뒤집은 다음 숫자형으로 바꾼다.

2. 수학적으로 계산하기
```javascript
    function solution(n) {
    var arr = [];

    do {
        arr.push(n%10);
        n = Math.floor(n/10);
    } while (n>0);

    return arr;
}
```
- n을 10으로 나눈 나머지는 n의 마지막 자릿수이다. 그 수를 빈 배열인 arr에 push해준다. 그런 다음 n을 10으로 나눈 몫을 n으로 지정해주고 n이 0이 될때까지 반복한다.

- 수학적으로 접근해서 푼게 새로웠고, 이러한 방법으로 자릿수를 배열할 수 있다는 것을 알았다.

### 새롭게 알게된 점
- do while문
while문은 테스트 조건이 거짓으로 평가될 때까지 do의 지정된 구문을 실행하는 루프를 만든다.

## level1 평균 구하기
### 풀이
```javascript
function solution(arr) {
    let sum = arr.reduce((acc,cur) => acc + cur,0) //배열의 요소들을 다 더해서
    return sum/arr.length // 배열의 길이로 나눠줌
}
```

## level1 정수 내림차순으로 배치하기

### 풀이
```javascript
function solution(n) {
    let arrN = Array.from(String(n),Number)
    arrN.sort(function(a,b){
        return b-a;
    });
   return parseInt(arrN.join(''))

}
```
n을 숫자를 요소하는 array로 만든 다음 내림차순을 하고 join을 이용하여 하나의 숫자로 만들어 준다.

- 삽질
결과값이 숫자형으로 나와야되는데 문자형으로 나온다는 것을 인지하지 못했다. 
typeof를 이용하여 문자형으로 나온다는 것을 알았고 parseInt을 사용하여 숫자형으로 바꿔 주었다.
### 다른 사람 풀이
```javascript
function solution(n) {
  const newN = n + "";
  const newArr = newN
    .split("")
    .sort() // 오름차순으로 정렬
    .reverse() // 오름차순을 뒤집어 내림차순으로 바꿈
    .join("");

  return +newArr; //+를 앞에 붙여 숫자형으로 바꿔줌.
}
``` 