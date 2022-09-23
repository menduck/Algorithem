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

## level1 없는 숫자 더하기
### 풀이
```javascript
function solution(numbers) {
    const sum = numbers.reduce((acc,cur)=>acc+parseInt(cur),0);
    return 45-sum ;
}
```
numbers는 0에서 9까지 중복 없는 정수 배열임으로 합이 45로 정해져있다. 
numbers의 없는 값의 합은 45에서 모두 더한 인풋값을 배면 된다.

### 보완
- 위의 코드는 정수 배열이 커지면 한계가 있다. 
- 이를 보완하기 위해서 정수 배열의 크기와 상관없는 코드를 짜야한다.
```javascript
function solution(numbers){
    let sum = 0;
    for(let i =0; i<numbers.length;i++){
        if(!(numbers.includes(i))){ //numbers에 i가 포함되지 않으면 i를 더한다.
            sum +=i
        }
    }
    return sum
}
```
## level1 내적
### 풀이
```javascript
function solution(a, b) {
    let sum = 0;
    for(let i=0;i<a.length;i++){
       sum += a[i]*b[i]
    } return sum
}
```
### 다른 사람 풀이
- reduce 사용해서 풀기
```javascript
function solution(a, b) {
    return a.reduce((acc, _, i) => acc += a[i] * b[i], 0);
}
```
- reduce(누적값,현재값,인덱스)
- 현재값이 없으니 _ 초기값으로 둔다.

## level1 문자열 내림차순으로 배치하기
### 풀이
```javascript
function solution(s) {
    return s.split('').sort().reverse().join('')
}
```
1. s.split('')
문자열을 sort가 용이하기 위해 array로 만든다.
2. sort().reverse()
정렬을 한 후 reverse를 이용하여 뒤집는다. => 내림차순
3. join('')
array를 다시 문자열로 만들어 준다.

## level1 문자열 다루기 기본
### 풀이
```javascript
function solution(s) {
    let sum = s.split('').reduce((acc,cur)=>acc+parseInt(cur),0)
   if (s.length == 4 || s.length == 6){
       if(isNaN(sum) != true){
           return true
       }else return false       
   }else 
       return false

}
```
문자열 s를 array로 만들어 각 요소들을 다 더한다.
그 sum의 길이가 4 또는 6이고, NaN이 아니면 true
그 외는 다 false
* 지수형태도 false가 나온다.

### 다른 사람 풀이
```javascript
function solution(s) {
    let result = parseInt(s)
    if((s.length==4||s.length==6) && result==s){
        return true
    }
    return false;
}
```
-parseInt
문자와 숫자가 섞여있으면, 숫자로 시작하면 연속되는 숫자까지만 정수 형태로 반환한다. 그 외는 NaN

parseInt의 특징을 이용하여 result==s가 같지 않다면 
1.숫자+문자 여서 문자가 변환되지 않아 같지 않은 경우 2.Nan인 경우 임으로 false를 반환한다.

## level1 약수의 개수와 덧셈
### 풀이
```javascript
//약수의 개수를 구하는 함수
function divisorCount(num){
    let countN =0;
    for(let i =1;i<=num;i++){
       if(num%i === 0) countN++
    }return countN
} 
// 약수의 개수 홀짝에 따라 더하고 빼는 함수
function soloution(left,right){
    let answer = 0;
    for(let j = left;j<=right;j++){
        if(divisorCount(j)%2===0){
            answer += j ;
        } else answer -= j;
    } return answer
}
```
### 삽질
1. 이중 for문으로 처음에 접근했는데 풀지 못했다. 아직 for문 개념이 확실히 잡히지 않은거 같다.
2. a^n*b^n의 약수의 개수는 (n+1)*(m+1) 로 접근했는데 소인수분해 코드 짜는 것을 실패했다.

### 다른 사람 풀이
```javascript
function solution(left, right) {
    var answer = 0;
    for (let i = left; i <= right; i++) {
        if (Number.isInteger(Math.sqrt(i))) {
            answer -= i;
        } else {
            answer += i;
        }
    }
    return answer;
}
```
약수의 개수가 홀수이면, 그 수의 제곱근은 정수이다. -> 제곱수의 약수는 +1이니깐

-이중 for문
```javascript
function solution(left, right) {
  let answer = 0;

  for (let i = left; i <= right; i++) {
    let count = 0; //약수의 개수 기본값설정
    for (let j = 1; j <= i; j++) {
      if (i % j === 0) count++; // 약수 조건이 되면 +1
    }
    if (count % 2) answer -= i;
    else answer += i;
  }

  return answer;
}
```
- count=0의 위치를 첫번째 for문 밖으로 빼서 제대로 카운팅이 되지 않았고, 약수를 array로 만들어서 그 array의 길이로 짝홀을 판단하려고 해서 더 복잡하게 코드를 짜려고 했다. 
- 약수를 배열 생성하지 않아도 카운팅 할 수 있는 법을 알았다.

## level1 행렬의 덧셈
### 풀이
```javascript
function solution(arr1, arr2) {
    let answer = [];
   for(let i =0;i<arr1.length;i++){
       let temp =[];
       for(let j=0;j<arr1[0].length;j++){
           temp.push(arr1[i][j]+arr2[i][j])
       } answer.push(temp)
       
   } return answer

}
```
처음 temp를 선언하지 않고 모두 answer에 푸시하도록 했더니 [4,6,7,9]로 array가 구분되서 나오지 않았다.
두번째 for문에서 임시로 temp를 놓고 array의 합이 나올때마다 push하고 2차 for문이 끝나면 비워지게 했다.

### 다른 사람 풀이
```javascript
function solution(left,right){
    return left.map((a,i)=>a.map((b,j)=> b+right[i][j]))
}
```
순차적으로 진행해보기
left=[[1,2],[3,4]];
right=[[5,6],[7,8]];

a=[1,2] i=0
a의 b는 1, j=0

1+right[0][0] = 1+5 =6 이런식으로 계산이 된다.

## level1 직사각형 별찍기
### 풀이
```javascript
process.stdin.setEncoding('utf8'); //입력을 받는 코드
process.stdin.on('data', data => { //입력값을 data로 받고 "5 3"
    const n = data.split(" "); //data를 띄어쓰기로 나눈다 n = [5,3]
    const a = Number(n[0]), b = Number(n[1]); // a=5,b=3
    console.log(("*".repeat(a)+'\n').repeat(b))
});
```
*를 a만큼 반복하고 엔터값로 구분하는 것이 1횡
횡을 b만큼 반복하여 직사각형을 만든다.

## level1 부족한 금액 계산하기
### 풀이
```javascript
function solution(price, money, count) {
    let pay = 0;
    //방문횟수만큼 곱해 pay에 더해줌.
   for(let i = 1;i<=count;i++){
       pay += price*i
   } 
   // 내야될 돈이 가진돈 보다 크면 그 차이를 반환한다. 아니면 0
    if(pay>money) {
        return pay-money
    } else return 0
}
```
주의! 0을 반환하고 싶으면 return 0 이다. return "0"이라 하지 말 것!

>> 마지막 조건문 삼항 연산자로 표현하기

return pay>money ? pay-money:0

### 다른 사람 풀이
```javascript
function solution(price, money, count) {
    const tmp = price * count * (count + 1) / 2 - money;
    return tmp > 0 ? tmp : 0;
}
```
가우스 공식을 이용해서 풀었다
등차수열 1~n까지의 합이 n(n+1)/2 에서 price곱해 내야할 돈을 구했다.
!!!!!!!!!!!!!코테 끝나고 다시 보기~!!!!!!!!!!!!!!!!!!

## level1 같은 숫자는 싫어
### 풀이
```javascript
function solution(arr)
{   
    let answer=[arr[0]];
    for(let i = 0;i<arr.length-1;i++){
       if( arr[i] != arr[i+1] ) answer.push(arr[i+1]) //요소 두개씩 비교. 각각 다르면 오른쪽 요소가 answer에 들어간다.
    } return answer
    
}
```
요소 두개씩 비교하여 다르면 두번째 요소가 answer에 들어간다.
인덱스0번의 요소가 들어가지 않는 것을 방지하여 처음 answer에 arr[0]를 미리 넣어 놓는다.

### 다른 사람 풀이
```javascript
function solution(arr){
    return arr.filter((v,i)=>v!= arr(i+1))

}
```
요소가 그 다음 요소와 다를때, 필터 처리되어 남는다.
마지막 인덱스의 값은 undefined랑 비교하게 되어 마지막 인덱스가 저장된다.

##
### 풀이
```javascript
function solution(s) {
    let arr = s.split(' '); 
    let answer = [];
    for(let i = 0;i<arr.length;i++){
        let temp = [];
        for(let j =0 ; j<arr[i].length;j++){
            if(j%2===0) temp.push(arr[i][j].toUpperCase())
            else temp.push(arr[i][j].toLowerCase())
        } answer.push(temp.join(''))
    } return answer.join(' ')
}
```
낱말을 array로 넣기 위해 s를 split로 띄어쓰기 기준으로 나눴다.
그 array를 for문을 이용하여 인덱스가 짝수이면 대문자 홀수이면 소문자로 반환한 값을 temp에 잠시  join으로 합쳐 넣었다.
answer값이 [TrY,HeLlO,WoRlD]로 되어있으므로 마지막에 join(' ')을 해주어 띄어쓰기로 구분하여 문자열로 변환한다.

### 삽질
s에 소/대문자가 섞일지 모르고 인덱스가 짝수일때 대문자로만 바꿔주고 , 홀수일때 소문자로 바꿔주지 않았다.

### 다른 사람 풀이
- map() 이용해서 풀기
```javascript
function solution(s) {

    let strArr = s.split(' ');

    let wordTransArr = strArr.map( (word) => word.split('').map( // [ 't', 'r', 'y' ]

        (curr, index) => index % 2 == 0 ? word[index].toUpperCase() : word[index].toLowerCase()                                  
    ).join(""));

    return wordTransArr.join(" ");

}
```
## level1 3진법 뒤집기
### 풀이
```javascript
function solution(n) {
   let reversedN = n.toString(3).split('').reverse().join('')
   return parseInt(reversedN,3)
}
```
1. Number.toString([radix])
: 숫자를 문자열로 변환하여 반환 / number를 radix(진수)의 값으로 변환한 값을 문자열로 반환
2. parseInt(string,radix)
: string값을 radix로 분석한 정수로 반환한다.

### 다른 사람 풀이
- 내장 함수를 몰랐을때 이렇게 풀고 싶었는데 재귀함수로 만들기 어려웠다. 
```javascript
function solution(n){
    const answer = [];
    while(n!==0){ //n이 0이 아니면
        answer.unshift(n%3); //n을 3으로 나눈 나머지를 answer에 추가한다.
        n = Math.floor(n/3); // n은 다시 3으로 나눈 몫이 된다.
    } return answer.reduce((acc,v,i)=>acc+(v*Math.pow(3,i)),0); // reverse할 필요없이 10진법을 만들어 줄때 반대로 계산하면 된다.
}
```
reverse가 되어 0*3^3 + 0*3^2 + 2*3^1 + 1*3^0 으로 십진법 변환 계산을 해줘야 되지만 인덱스를 차례대로 주어
1*3^0 + 2*3^1 + 0*3^2 + 0*3^3 로 계산하고 reduce를 사용해 누적해서 합을 반환한다.

## level1 예산
### 풀이
```javascript
//최대 지원할 수 있는 부서의 수 구하는 함수
function solution(d, budget) {
    let sum = 0, caseN = 0;
   d.sort((a,b)=>a-b);
    for (let i = 0;i<d.length;i++){
     sum += d[i]
        if(sum <= budget)
            caseN++
    } return caseN++
}
```
- 최대 지원할 수 있는 부서의 수를 구해야하기 때문에, 제일 작은 예산이 필요한 부서를 꼭 필요하다
- d를 오름차순으로 정렬한 다음 요소들을 누적합계하여 몇 개의 부서의 신청예산이 예산 값보다 같거나 작은지 카운팅 해준다.

## level1 시저암호
### 풀이
- AaBbCc~를 기준값으로 잡고 기준값의 인덱스값을 i+(n*2)로 넣고 뽑아서 answer값에 push하고 싶었는데 실패했다.
- 아스키코드값을 이용해서도 풀 수 있다.

```javascript
function solution(s, n) {
    var upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var lower = "abcdefghijklmnopqrstuvwxyz";
    var answer= '';

    for(var i =0; i <s.length; i++){
        var text = s[i];
        if(text == ' ') {
            answer += ' '; 
            continue;
        }
        var textArr = upper.includes(text) ? upper : lower;
        var index = textArr.indexOf(text)+n;
        if(index >= textArr.length) index -= textArr.length;
        answer += textArr[index];
    }
    return answer;
}
```
-아스키값 이용한 함수
```javascript
function solution(s, n){
    return s.split("").map(value => {
        if (value === " ") return value; //공백이 있다면 그대로 공백값을 준다.
        return value.toUpperCase().charCodeAt() + n > 90 //Z를 초과한다면
        ? String.fromCharCode(value.charCodeAt() + n - 26) //26(알파벳 개수)를 빼준다
        : String.fromCharCode(value.charCodeAt() + n)// 그게 아니라면 n값을 더한 값을 문자로 반환해준다.
    }).join("");
}
```
## level1 [1차]비밀지도
```javascript
function solution(n, arr1, arr2) {
 let binaryArr1 = arr1.map(v=>v.toString(2).padStart(n,0)); //n에 맞게 앞에 0을 채워줌
 let binaryArr2 = arr2.map(v=>v.toString(2).padStart(n,0));
    answer = [];
    for(let i =0;i<n;i++){ //이진수가 된 arr두개를 문자열로 합친다.
        let temp =[]
        for(let j =0;j<n;j++){
        temp.push(binaryArr1[i][j] + binaryArr2[i][j])
        } answer.push(temp)
    }  return answer.map(a=>a.map(b=>{ //안에 있는 요소가 00이면 공백을 나머지는 #을 반환하고 join한다.
        if(b!=='00') return '#';
        else return ' ';

    }).join(''))
```
## level1 최소직사각형
### 풀이
```javascript
function solution(sizes) {
    let w = sizes.map(v =>v[0]);
    let h = sizes.map(v =>v[1]);

    for(let i =0; i<sizes.length;i++){
        if(w[i]<h[i]){
            let temp = w[i]; //w와 h 자리 바꾸기 위해 임시로 temp에 w를 넣어 놓는다.
            w[i] = h[i];w
            h[i] = temp;
        }
    } return Math.max(...w)*Math.max(...h)
}
```
-temp에 넣어놓을 필요 없이 map으로 하는 법
const rotated = sizes.map(([w,h])=>w<h?[h,w]:[w,h]);

## level1 문자열 내 마음대로 정렬하기
### 풀이
```javascript
function solution(strings, n) {
    let strN=[];
    for(let i =0;i<strings.length;i++){
        strN.push(strings[i][n])
    } 
    strN.sort()
    let answer =[];
    for(let j =0;j<strings.length;j++){
        for(let k = 0;k<strings.length;k++){
            if(strN[j] == strings[k][n])
                answer.push(strings[k])
        } 
    } return answer
   
     
}
```
-n번째 인덱스 값이 중복되면 사전순으로 정렬되야되는데, 예외 처리에 실패했다.

### 다른 사람 풀이
```javascript
function solution(strings, n) {
    strings.sort((a,b)=>{
        if(a[n]>b[n]){ // a[n]이 더 크면
            return 1 // 그대로
        } else if (a[n]<b[n]){ //a[n]이 더 작으면
            return -1 //뒤로 보낸다
        } else{ // 주어진 인덱스가 같을 경우
            if(a>b){ //문자열을 비교한다.
                return 1;
            } else return -1;
        }
    })
    return strings
}
```

## level1 K번째 수
### 풀이
```javascript
function solution(array, commands) {
    // i~j까지 문자열 자른다.
    let newArr=[];
    for(let i =0;i<commands.length;i++){
    let temp = array.slice(commands[i][0]-1,commands[i][1]);
    newArr.push(temp)
    }  // 자른 문자열 정렬
        result = [];
        for(let j=0;j<commands.length;j++){
        result.push(newArr[j].sort((a,b)=>a-b))
            
    } // k번째 원소 반환한다.
    return result.map((v,i)=>v[commands[i][2]-1])
}
```
-같은 방식이지만 좀 더 정리된 코드
```javascript
function solution(array,commands){
    let answer=[];
    for(let i =0;i<commands.length;i++){
        let num = commands[i];
        let slicedArr = array.slice(num[0]-1,num[1]);
        answer.push(slicedArr.sort((a,b)=>a-b)[num[2]-1])
    } return answer;
}
```

## level1 숫자 문자열과 영단어
### 풀이
```javascript
function solution(s) {
    s = s.replace(/zero/gi, 0)
    .replace(/one/gi, 1)
    .replace(/two/gi, 2)
    .replace(/three/gi, 3)
    .replace(/four/gi, 4)
    .replace(/five/gi, 5)
    .replace(/six/gi, 6)
    .replace(/seven/gi, 7)
    .replace(/eight/gi, 8)
    .replace(/nine/gi, 9)
    return Number(s);
} 
```
g는 모든 내용 교체, i는 대소문자 구별하지 않는 것을 의미한다.

### 다른 사람 풀이
```javascript
function solution(s) {
    let numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    var answer = s;

    for(let i=0; i< numbers.length; i++) {
        let arr = answer.split(numbers[i]);
        answer = arr.join(i);
    }

    return Number(answer);
}
```
!!!!!!!!!!!!!!!!!다시 한번!!!!!!!!!!!!!!! https://jaekwan.tistory.com/127

## level1 두 개 뽑아서 더하기
### 풀이
```javascript
function solution(numbers) {
   const sortedNum = numbers.sort((a,b)=>a-b); //정렬부터 해준다.
    let allnum = [];
    // 더할 수 있는 모든 경우의 수를 allnum에 저장한다.
    for(let i =0;i<numbers.length;i++){
        for(let j=0;j<numbers.length;j++){
        if(i!=j){
            allnum.push(numbers[i]+numbers[j])
        }
    } 
    } // 중복되는 경우의 수를 제거하고 오름차순으로 나타낸다.
    let result = [...new Set(allnum)].sort((a,b)=>a-b)
    return result

}
```
- set()을 한다고해서 다 오름차순으로 되는 건 아니다.
- i != j 조건으로 할 필요없이 j=i+1로 설정하면 자기 자신을 더하는 경우의 수가 빠진다.

## level1 2016년
### 풀이
```javascript
function solution(a, b) {
    let date = new Date(2016,a-1,b).getDay() 
   const week =['SUN','MON','TUE','WED','THU','FRI','SAT'];
    return week[date]
   
}
```
- new Data(년,월,일)
날짜를 숫자로? 변환시켜줌. 월은 0부터 11까지다 1월은 0 주의하자.

## level1 포켓몬
### 풀이
```javascript
// 가질 수 있는 포켓몬의 종류의 수를 구하는 함수
function solution(nums) {
    let getNum = (nums.length) /2
    let newNums = [...new Set(nums)].sort((a,b)=>a-b)
    if(newNums.length >= getNum){
        return getNum
    } else
        return newNums.length
}
```
## level1 소수찾기
### 풀이
```javascript
//소수 찾기
function primeNum(num) {
    for(let i =2;i<=Math.sqrt(num);i++){ 
    if(num%i===0) return false; //2부터 제곱근까지 한번이라도 나눠떨어지면 소수가 아님.
    } return true;
}
//2~n까지 소수의 개수 구하는 함수
function solution(n){
    let result =0
    for(let j=2;j<=n;j++){
        if(primeNum(j)) result++
    } return result
}
```
