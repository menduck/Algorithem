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
## level1 문자열 내 p와 y의 개수
### 풀이
```javascript

function solution(s){
    //s 문자열을 전부 소문자로 바꿔줌.
    let arr = Array.from(s.toLowerCase());
    let countNumP = 0;
    let countNumY = 0;

    for(let i = 0; i < arr.length; i++)
    // 문자열 요소 중 p가 있으면 카운팅이 됨.
        if(arr[i] === 'p'){
        countNumP++
        }
    // 문자열 요소 중 y가 있으면 카운팅이 됨.
        else if(arr[i]==='y'){
            countNumY++
        }
    if(countNumP === countNumY){
        return true;
    } else
       return false;

}
```

### 다른 사람 풀이
```javascript
function numPY(s){
  var result = true;
  s = s.toUpperCase();
  var num = 0;
  for(var i = 0; i < s.length; i++){
    if(s[i] === 'P') num++;
    if(s[i] === 'Y') num--;
  }
  result = (num === 0);

  return result;
}
```
-나와 비슷한 코드이지만 P와 Y의 카운팅을 따로 세지 않고, 하나는 양수로 하나는 음수로 개수를 세어 똑같은 개수이면 합이 0이 나오는 코드이다.

```javascript
function solution(s){
    return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
}
```
- 문자열을 대문자로 바꾸고, 'P'문자로 문자열을 나눈 다음 길이를 구한다. 그 길이가 'Y'문자로 문자열을 나눈 길이와 같다면 true, 다르다면 false를 return한다.

## level1 하샤드 수
### 풀이
```javascript
function solution(x) {
 let newArr = Array.from(String(x),Number);
 let newArrSum = newArr.reduce((acc,cur) => acc + parseInt(cur),0);
 return x%newArrSum ===0
}
```
## level1 문자열을 정수로 바꾸기
### 풀이
```javascript
function solution(s) {
    return +s
}
```
s열에 -가 있으면 '-'+'parseInt(s)가 return되도록 코드를 짰다가, 문자열을 그냥 숫자로 바꾸면 조건이 필요없다는 것을 알게되었다. 

## level1 x만큼 간격이 있는 n개의 숫자
### 풀이
```javascript
function solution(x, n) {
    let answer = []; //빈 문자열을 만들어 주고
    for(let i =1; i <= n;i++){
        answer.push(x*i) // x값에 최대 n만큼 1씩 증가하여 곱해주면 값들을 다 push함.
    }
    return answer
}
```
### 다른 사람 풀이
```javascript
function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
```
1. Array(n).fill(x)
array안에 n개의 요소들이 x로 채워져있다.
예를 들어, Array(5).fill('s') 은 ['s', 's', 's', 's', 's'] 값이 나온다.

2. .map((v, i) => (i + 1) * v)
x로 채워진 array을 map()을 통해 각각 불러와 현재값과 인덱스+1의 값을 곱해 배열을 생성한다.

## level1
### 풀이
```javascript
function solution(num) {
    let caseNum = 0
    // num가 1이면 0을 return함
    if (num === 1)  {
       return 0
    } 
    //문제 작업을 반복하면서 카운트를 센다.
    while(true){
        if(num%2 ===0){
            num = num/2
        }else
            num = num*3+1
        caseNum++
    // num가 1이 되면 루트에서 빠져 나온다.
   if (num === 1){
       break
   }
    }
    // caseNum가 500을 넘으면 -1을 출력하고 나머지는 caseNum를 출력한다.
    if(caseNum >= 500){
        return -1
    } else 
    return caseNum
}
```
가독성이 떨어져 정리가 필요하다.
삼항연산자를 사용하여 다시 풀어보았다.
```javascript
function solution(num) {
    let caseNum = 0
    
    while(true){
        if(caseNum>=500){
            return -1;
        }else if(num != 1){
            (num%2) ? num=num*3+1 : num=num/2;
        }else if(num ===1){
            return caseNum;
        }
        caseNum++;
    }
    return caseNum
}
```
1. (num%2) ? num=num*3+1 : num=num/2;
조건 ? ture : false
num%2 가 0이면 false임을 주의하자! 0이면 홀수임으로 num*3+1을 해주고 (num%2)가 0이 아닌 수이면 true임으로 num/2를 해준다.

## level 두 정수 사이의 합
### 풀이
```javascript
function solution(a, b) {
    let numberArr = [];
    //a,b의 대소관계 정리
    let maxNum = Math.max(a,b);
    let minNum = Math.min(a,b);
    //a와 b사이에 속한 정수 배열 생성
    for(let i=minNum;i<=maxNum;i++){
        numberArr.push(i)
    }
    //정수의 합
    return numberArr.reduce((acc,cur)=>acc+parseInt(cur),0)
}
```
최종 정리
```javascript
function solution(a, b) {
    let sum = 0;
    let maxNum = Math.max(a,b);
    let minNum = Math.min(a,b);
    for(let i=minNum;i<=maxNum;i++){
        sum += i
    }
    return sum
}
```
처음부터 배열을 생성할 필요가 없었다. 배열을 만들지 않고 바로 더해서 결과값을 구할 수 있다.

### 다른 사람 풀이
```javascript
function solution(a, b) {
   return (a+b)*(Math.abs(b-a)+1)/2
}
```
등차수열 공식을 이용해서 간단하게 풀 수 있다.
- 1부터 n까지의 합 공식은 n*(n+1)/2이다.
- n부터 m까지의 합 공식은 (n~m의 개수)*(n+m)/2이다.

수학 공식을 더 알고있으면 더 쉽고 간단하게 풀었을 거 같다! 간단한 수학 공식정도는 기억해 두자.

## level 서울에서 김서방 찾기
### 풀이
```javascript
function solution(seoul) {
    for(let i=0;i<seoul.length;i++){
        if(seoul[i] === "Kim"){ //요소들 중 "Kim"이 있으면
            let kimIndexNum = seoul.indexOf("Kim") //kim의 index번호 찾는 코드
            return `김서방은 ${kimIndexNum}에 있다`
        }
    }
}
```
### 다른 사람 풀이
```javascript
function solution(seoul) {
   
            let kimIndexNum = seoul.indexOf("Kim")
            return `김서방은 ${kimIndexNum}에 있다`
        }
```
요소들 중 kim이 있으면, kim의 인덱스 번호를 찾는 코드를 짰는데, 다른 풀이를 보면 굳이 조건을 달 필요가 없었다.... kim의 인덱스 번호가 있다는 말이 요소들 중 kim이 있다는 말이기 때문이다.

## level1 핸드폰 번호 가리기
### 풀이
```javascript
function solution(phone_number){
    const phone_numberLength = phone_number.length;
    const vaildPhonenumber = phone_number.slice(-4);
    let answer=[];
    for(let i =1;i<=phone_numberLength-4;i++){
        answer += "*"
    }
    return answer+vaildPhonenumber
}
```
- slice을 이용하여 번호 뒷자리 4개를 구하고, 번호 길이를 구해 뒤에 4자리뺀 나머지를 "*"로 채운다.

아쉬운 점
- for문으로 "*"을 채운 방법 말고 더 간단한 방법이 있을 거 같다.
- 변수명이 아쉽다. star말고 hide가 더 알기 쉬울 거 같다.

### 다른 사람 풀이
```javascript
function solution(phone_number){
    let hide_number = ''

    for(let i=0;i<phone_number.length;i++){
        hide_number += i < phone_number.length-4 ? "*" : phone_number.charAt(i);
    };
    return hide_number ;
}
```
1. for(let i=0;i<phone_number.length;i++){
        hide_number += i < phone_number.length-4 ? "*" : phone_number.charAt(i);
    };

    뒤에서 4번째 숫자가 되기 전까지 "*"이 누적되고, 뒤에서 4번째 자리부터 번호의 단일문자가 반환된다.

- repeat이용해서 풀기

```javascript
function hide_numbers(s){
  var result = "*".repeat(s.length - 4) + s.slice(-4);


  return result;
}
```
for문을 사용하지않고 간단하게 repear사용하여 반복한다.

-정규 표현식 활용해서 풀기
```javascript
function hide_numbers(s) {
  return s.replace(/\d(?=\d{4})/g, "*");
}
``` 
!!!이해못함 다시 해보기

- fill,join 사용해서 풀기
```javascript
function solution(phone_number){
    return [...phone_number].fill('*',0,phone_number.length-4).join('')
}
```
전개 문법을 이용해 배열로 만든다.
 '*'을 처음부터 뒷 자리 4번째 전까지 채워주고 join으로 문자열로 만들어 준다.


### 새로 배운 문법
- str.charAt(index)
 문자열 내의 단일 문자를 반환시켜줌.
 만약 인덱스가 문자열 길이보다 큰 경우 빈 문자열 ""을 반환함.

## level1 제일 작은 수 제거하기
### 풀이
- 작은 수가 중복된다면 다 제거하기 => 하지만 조건에선 중복이 없다고 했음(나중에 앎.)
- 정렬이 아님
```javascript
function solution(arr) {
    // min값 설정
    const minNum = Math.min(...arr)
    // 차례대로 순회하면서 min값을 제거함.
    for(let i =0;i<arr.length;i++){
        if(arr[i] === minNum){
            arr.splice(i,1);
        } 
    // arr의 길이가 0이라면 [-1]출력하게 함.
    } if(arr.length === 0){
        return [-1]
    } else
        return arr
}
```
### 삽질
minNum를 for문 안에 넣어서 minNum가 변경되어 2번째 작은 수도 같이 삭제되었다.
for문 밖에 min값을 구하고, for문 안에서 그 min값을 찾아 삭제해야한다.

-'인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.' 라는 뜻이 '중복이 없다'라고 바로 해석하지 못했다.

### 다른 사람 풀이
```javascript
function solution(arr) {
    arr.splice(arr.indexOf(Math.min(...arr)),1); //중복된 수가 없기 때문에 indexOf를 써도 됨.
    if(arr.length<1)return[-1];
    return arr;
}
```
- filter 이용해서 풀기
```javascript
function solution(arr) {
    const min = Math.min(...arr);
    return arr.length !== 1 ? arr.filter(i => i !== min) : [-1]
}
```
1. arr.filter(i => i !== min)
요소 중 min이 아닌 요소들만 추출하여 arr을 생성한다.

## level1 나누어 떨어지는 숫자 배열
### 풀이
```javascript
function solution(arr, divisor) {
    let newArr = arr.filter(i => i%divisor === 0 ) //요소들이 divisor값으로 나눈 나머지가 0인 경우만 필터 처리 됨.
    if(newArr.length === 0){
        return [-1]; //빈 배열이면 [-1] return
    }else
        return newArr.sort((a,b)=>a-b); //오름차순
}
```
### 삽질
```javascript
function solution(arr, divisor) {
    return arr.filter(i => i%divisor === 0 ? arr.sort((a,b)=>a-b):[-1])   
}
```
- 삼항연산자를 사용하고 싶었는데 실패함.

### 최종 코드
```javascript
function solution(arr,divisor){
    let newArr = arr.filter(i => i%dicisor ===0);
    return newArr.length === 0? [-1]:newArr.sort((a,b)=>a-b);
}
```
- divisor로 나눈 나머지가 0이되는 newArr를 뽑아낸 후 삼항연산자로 return을 해줘야 한다.

## 음양 더하기
### 풀이
```javascript
function solution(absolutes, signs) {

    for(let i =0;i<absolutes.length;i++){
        if(signs[i]===false){
            absolutes.splice(i,1,-absolutes[i]);
        }
    } return absolutes.reduce((acc,cur)=>acc+parseInt(cur),0)
}
```
-for문이 signs을 순회하면서 false인 인덱스를 발견하면 absolutes와 똑같은 인덱스를 찾아 음수로 바꿔준다.
그 다음 배열의 모든 수를 reduce를 사용하여 더해준다.

### 다른 사람 풀이
```javascript
function solution(absolutes, signs) {

    return absolutes.reduce((acc, val, i) => acc + (val * (signs[i] ? 1 : -1)), 0);
} 
```
signs이 true이면 바로 absolutes의 해당 요소에 1를 곱해 더한다. 만일 false이면 -1을 곱해 더한다.
다르 사람들 의견으론 reduce보다 for문이 빠르고 해당 코드가 가독성이 떨어지기 때문에 멋진 코드이지만 좋은 코드는 아니라 판단한다.

-forEach를 사용하여 풀기
```javascript
function solution(absolutes,signs){
    let answer = 0;
    absolutes.forEach((v,i)=> {
        if(signs[i]){ //true이면
            answer += v; 
        } else{
            answer -= v;
        }
    }) 
    return answer;
}
```
### 새롭게 알게 된점
-forEach
파라미터로 주어진 함수를 배열 요소 각각에 대해 실행하는 메서드
map()과 다른 점은 return값이 필요하지 않다는 점이다. 새로운 배열을 생성하지 않으면 forEach를 활용하자.

let arr=[1,2,3];
arr.forEach((el,index,array) => {console.log(el);console.log(index),console.log(array)})
//
1
0
[ 1, 2, 3 ]
2
1
[ 1, 2, 3 ]
3
2
[ 1, 2, 3 ]

## level1 수박수박수박수박수박수?
### 풀이
```javascript
function solution(n) {
    // n이 짝수일때 "수박"을 n/2만큼 출력함.
   if(n%2 ===0){
       return "수박".repeat(n/2);
   } else {
    // n이 홀수일때 +1을 하여 짝수로 만들어 수박문자열을 출력하고 마지막 문자열을 제거함.
       let newStr = "수박".repeat((n+1)/2);
    return newStr.slice(0,-1)
   }
}
```
### 다른 사람 풀이
```javascript
function solution(n){
    return "수박".repeat(n).slice(0,n)
}
```
repeat()값에 구애 받지 않아도 됨. 왜냐? slice에서 n만큼 잘라버리면 되니깐!

## level1 가운데 글자 가져오기
### 풀이
```javascript
function solution(s) {
    const sLength = s.length
 if(s.length%2 ===0){
     return s.slice(sLength/2-1,sLength/2+1)
 } else
     return s.charAt(sLength/2) // (sLength+1/2)-1이지만 자동 내림으로 계산됨으로 /2하였다.
}
```
### 다른 사람 풀이
```javascript
function solution(s){
    const mid = Math.floor(s.length/2);
    return s.length%2===0? s[mid-1]+s[mid] : s[mid]
}
```

1. s[mid-1]+s[mid]
s[i]가 문자열임으로 계산되지 않고 string타입으로 return한다.
