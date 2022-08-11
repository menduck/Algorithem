 
#백준 알고리즘 문제 풀기 시작(7/24~)

## 2022.7.24
## 1000 1001 10998 1008번

백준 사이트인 경우 입출력을 직접 작성해 줘야함.

### 입출력 방식 : fs모듈, readline모듈

    * fs모듈

    ```javascript

    const fs = require('fs'); //file system 모듈 불러옴

    //fs모듈의 readFileSync 를 통해 동기적으로 해당 경로의 파일 전체를 읽어들임
    //백준에선 '/dev/stdin' 경로에 테스트 케이스 파일이 있음.
    //읽어드린 정보는 toString함수를 통해 문자열로 변환
    //입력 받은 문자열은 split 함수를 통해 배열화한다.
    const inputData1 = fs.readFileSyns('/dev/stdin').toString().split('');

    //옵션을 사용하여 'utf8' 문자열로 반환
    const inputData2 = fs.readFileSync(0,'utf8').split('');

    ```
    

    * readline 모듈

    ```javascript

    const readline = require('readline');
    const rL=readline.createInterface({
        input : process.stdin,
        ouput : process.stdeout,
    });

    rL.on('line',(line) =>{
        //line을 가공하여 변수에 저장
    }).on('close,() => {
        //저장된 변수를 이용하여 계산 후 출력
    });
    // 각 줄이 입력될 때마다 'line'이벤트가 매번 발생하여 이를 변수에 저장하며, 'close'이벤트가 발생한 경우 저장된 변수를 가지고 계산을 진행.

    ```

### 결론
로직 도중 유저로부터 입력을 받거나 출력을 요하지 않기 때문에, 복잡한 readline 모듈보다 fs모듈을 통해 간결하게 작성.

### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(' '); // 문자열로 반환
const A = parseInt(inputData[0]); //숫자로 형변환 시킴
const B = parseInt(inputData[1]);

console.log(A+B);
console.log(A-B);
console.log(A*B);
console.log(A/B);
```

* 참조 https://leeph.tistory.com/48?category=664147

## 10869 사칙연산

### 문제
    * 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
    * 입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
    * 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

### 해설

```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(' '); 
//split을 이용하여 띄어쓰기를 없앰

const A = parseInt(inputData[0]); 
const B = parseInt(inputData[1]);
console.log(A+B);
console.log(A-B);
console.log(A*B);
console.log(Math.floor(A/B));
console.log(parseInt(A/B));
console.log(A%B);
```

### 주의
나누기 몫을 출력할때 소수점자리까지 출력된다.
Math.floor을 이용하여 소주점을 버리거나 parseInt를 이용하여 정수로 출력한다.

## 10926번

### 문제
    * 준하는 사이트에 회원가입을 하다가 joonas라는 아이디가 이미 존재하는 것을 보고 놀랐다. 준하는 놀람을 ??!로 표현한다. 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오.
    * 입력 : 첫째 줄에 준하가 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어진다. 아이디는 알파벳 소문자로만 이루어져 있으며, 길이는 50자를 넘지 않는다.
    * 출력 : 첫째 줄에 준하의 놀람을 출력한다. 놀람은 아이디 뒤에 ??!를 붙여서 나타낸다.

### 풀이
```javascript
const fs = require('fs');
const id = fs.readFileSync(0,'utf8').toString().trim(); 
//띄어쓰기로 나누는 것이 아니므로 문자열의 가장 앞부분과 가장 뒷부분의 공백을 지워주는 trim을 이용한다.
console.log(`${id}??!`);
```
### 참고
```javascript
a = "a 1 2 3 4 "
b = "a 1 2 3 4"
console.log(a.split(" ")); //['a', '1', '2', '3', '4', ''] //마지막 항목 다음에 띄어쓰기까지 array에 들어감.
console.log(b.split(" ")); //['a', '1', '2', '3', '4']
console.log(a.trim()); // a 1 2 3 4 
```

## 2022.07.25
## 18108번 1998년생인 내가 태국에서는 2541년생?
### 문제
    * 불교 국가인 태국은 불멸기원(佛滅紀元), 즉 석가모니가 열반한 해를 기준으로 연도를 세는 불기를 사용한다. 반면, 우리나라는 서기 연도를 사용하고 있다. 불기 연도가 주어질 때 이를 서기 연도로 바꿔 주는 프로그램을 작성하시오.
    * 서기 연도를 알아보고 싶은 불기 연도 y가 주어진다. (1000 ≤ y ≤ 3000)
    * 불기 연도를 서기 연도로 변환한 결과를 출력한다.

### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString();
const immoralOrigin = parseInt(inputData);
console.log(immoralOrigin-543) ;
```
fs모듈을 이용하여 inputData값을 받고 그 값을 parseInt를 이용해 숫자로 형변환시킴. 불원기원 = 서기 -543 임으로 간단하게 console.log에서 계산해줌

## 10430번 나머지
### 문제
    * (A+B)%C는 ((A%C) + (B%C))%C 와 같을까? (A×B)%C는 ((A%C) × (B%C))%C 와 같을까? 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
    * 첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)
    * 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");
const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);
const C = parseInt(inputData[2]);

const result1 = (A+B)%C ;
const result2 = ((A%C) + (B%C))%C;
const result3 = (A*B)%C ;
const result4 = ((A%C)*(B%C))%C ;

console.log(`${result1}\n${result2}\n${result3}\n${result4}`);
```
벡터를 이용하여 `${변수}\n`꼴로 만들어 줄마다 값을 출력시켰다.

### 참고
* 다른 코드와 비교
    - 입력값을 array로 받아 활용
    ``` javascript
    const [A,B,C] = inputData ;
    ```
* 문자열을 숫자열로 형변환 하는 방법
    1.parseInt() 
    문자열을 '정수'로 변환
    '숫자+문자'꼴은 숫자만 출력 '문자+숫자'꼴은 NaN
    ```javascript
    const test = parseInt("123가나다");
    const test2 = parseInt("가나다123");
    console.log(test); // 123
    console.log(test2); // NaN
    ```

    2.Number()
    문자열을 '숫자'로 변환 (소수점까지 숫자타입으로 가져 올 수 있음.)
    숫자꼴만 리턴하고 문자가 들어가면 NAN
    ```javascript
    const test = Number("123가나다");
    const test2 = Number("가나다123");
    console.log(test); // Nan
    console.log(test2); // NaN
    ```
## 2588번 곱셈
### 문제
    *(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
![2588](https://user-images.githubusercontent.com/39366835/182073387-fafdec42-2ace-4be7-a8ef-59a3208c3726.png)

    * 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
    * 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split("\n")
const A = parseInt(inputData[0]) ; // 숫자
const B = inputData[1] ; //array를 하기 위해 문자열로 둠.
const strArr = Array.from(B); // array로 만듦

const result3 = A * parseInt(strArr[2]); // strArr를 숫자로 만들어 계산함
const result4= A * parseInt(strArr[1]);
const result5 = A * parseInt(strArr[0]);
const result = A * B ;

console.log(`${result3}\n${result4}\n${result5}\n${result}`);
```
### 참고
 * 숫자를 array로 바꾸는 방법
    ```javascript
    const number = 123456; //숫자
    const str = String(number); //문자열로 바꿈
    const array = Array.from(str);// str를 배열로 바꿈
    console.log(array); //['1', '2', '3', '4', '5', '6']
    ```
* split으로 숫자 나누기
    ```javascript
    const num = 123456;
    const nStr = String(num);
    const sNum = number.split("");
    console.log(sNum); // ['1', '2', '3', '4', '5', '6']

## 25083번 새싹
### 문제
    * 아래 예제와 같이 새싹을 출력하시오.
    * 입력은 없고 출력은 새싹을 출력한다.

### 해결
```javascript
console.log(`         ,r'"7
r\`-_   ,'  ,/
 \\. ". L_r'
   \`~\\/
      |
      |`);
```

* `(백틱)을 사용해서 여러 줄 출력하게 만들었다. 주의할 점은 출력값 안에 백틱과 \가 있다면 \를 앞에 추가적으로 입력해야 한다. `\ \\

## 2022.07.29
## 1330번 두 수 비교하기
### 문제
    * 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
    * 첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
    * 첫째 줄에 다음 세 가지 중 하나를 출력한다.

      A가 B보다 큰 경우에는 '>'를 출력한다.
      A가 B보다 작은 경우에는 '<'를 출력한다.
      A와 B가 같은 경우에는 '=='를 출력한다.
    * -10,000 ≤ A, B ≤ 10,000

### 해결
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");
//공백 한 칸으로 구분되어져 있기 때문에 split(" ")
const A = Number(inputData[0]); // 문자열을 숫자형으로 바꾸고 array 안에 첫번째 항목 값을 가져옴
const B = Number(inputData[1]);

if (A > B) {
    console.log (">");
} else if (A < B) {
    console.log("<");
} else {
    console.log("==");
}
```

### 삽질
```javascript
else ( A === B){
    console.log("==");
}
```

else문에 조건을 달아 런타임에러가 났다. else에는 if, else if문에 모두 해당하지 않으면 실행되는 조건문이다! 헷갈리지 말 것.

## 9498번 시험성적

### 문제
    * 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
    * 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
    * 시험 성적을 출력한다.
### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString();

if (inputData >= 90){
    console.log("A"); //inputData가 90점 이상이면 A가 출력 됨.
} else if (inputData >= 80){
    console.log("B");
} else if ( inputData >= 70){
    console.log("C");
} else if (inputData >= 60){
    console.log("D");
} else {
    console.log("F"); // 조건문에 다 해당 안되면 F
}
```
if문을 이용하여 풂.

## 2022.08.01
## 2753번 윤년
### 문제
    *연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
    윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
    예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
    *첫째 줄에 연도가 주어진다. 연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
    *첫째 줄에 윤년이면 1, 아니면 0을 출력한다.
### 풀이
``` javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString();

if ( inputData % 4 ===0 && inputData % 100 !== 0 || inputData % 400 === 0){
    console.log("1")
} else {
    console.log("0");
}

```
* if문을 사용하여 조건문을 만듦
- inputData값이 4배의 배수가 된다는 것은 4로 나누었을때 나머지가 0임을 뜻함
- 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수임으로 4의 배수 and (100의 배수 아님 OR 400의 배수) 라고 수식을 정의해야 함.

### 참고

* AND operator
```javascript
if(age >=18 && age <=50) //18세 이상 50세 이하
```
true && true 만 true
true && false 이면 false

*OR operator
```javascript
if(age >=18 || age <=50) //18세 이상 또는 50세 이하
```
하나의 조건만 true여도 true

## 2022.08.09
## 14681번 사분면 고르기
### 문제
    * 사분면은 아래 그림처럼 1부터 4까지 번호를 갖는다. "Quadrant n"은 "제n사분면"이라는 뜻이다. 
    
    예를 들어, 좌표가 (12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.

    점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램을 작성하시오. 단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
    * 첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)

    * 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split("\n");
//fs모듈로 inputData 값을 받음. 엔터로 값이 분리 되어 있기 때문에 split으로 값을 받음

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

// and 연산자를 사용하여 if문으로 값을 도출 받음.

if (A > 0 && B > 0){ // A,B 모두 0 보다 큰 값이면
    console.log("1"); // "1" 를 출력함
} else if (A < 0 && B > 0){ // A가 0보다 작고 B가 0보다 크면
    console.log("2"); // "2" 를 출력함.
} else if (A < 0 && B < 0){
    console.log("3");
} else if ( A > 0 && B < 0 ) {
    console.log("4");
}
```
## 2022.08.10
## 2884번 알람 시계
### 문제 요약
    * 현재 상근이가 설정한 알람 시각이 주어졌을 때, 창영이의 방법(45분 일찍 알람 설정하기)을 사용한다면, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
    * 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
    입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
    *첫째 줄에 상근이가 창영이의 방법을 사용할 때, 설정해야 하는 알람 시간을 출력한다. (입력과 같은 형태로 출력하면 된다.)
### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");

const A = parseInt(inputData[0]); //시간
const B = parseInt(inputData[1]); //분

const totalM = (A*60+B)-45; // 시각을 분 단위로 바꾸고 -45분을 해줌

// 시간 조건이 (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 임으로 "24 00" 나오지 않게 if문 사용
if (totalM >0){ //계산된 시간이 0 초과일때
const resultA = Math.floor(totalM / 60); // 60으로 나누어 내림한 시간 출력
const resultB = totalM % 60 ; // 60으로 나눈 나머지로 분 출력
console.log(resultA, resultB);

} else if (totalM < 0 ){ //계산된 시간이 0 미만일때
const totalM1 = 1440 + totalM; 
// 24*60 시간에 음수가 된 totalM을 더함
// A = 0 , B = 1 일때 totalM = -44이다. 24시간에서 totalM을 더해 나타냄
const resultAA =  Math.floor(totalM1 / 60);
const resultBB = totalM1 % 60;
console.log(resultAA, resultBB);

} else if (totalM === 0){ //계산된 시간이 0일때 "24 00"이 출력되지 않도록 따로 출력값을 설정.
    console.log("0 0");
}
```
### 참고사항
* 너무 어렵게 푼 거 같다. 다른 블로그를 참고해보니 let을 사용해서 변수값을 계속 업데이트하여 간단하게 풀었다.
*변수명 설정이 아쉽다. A,B 보다는 시간과 분이 나타내니 H,M이 더 보기 편할 거 같다.

```javascript
let fs = require('fs');
let inputData = fs.readFileSync(0,'utf8').toString().split(" ");

let H = parseInt(inputData[0]);
let M = parseInt(inputData[1]);

solution(H,M);

function solution(H,M){
    if(M>=45){
        console.log(H,M-45); // M이 45이상이면 H값 변경없이 M값만 -45 연산해주면 됨.
    } else if(M<45){ // M이 45이상일때 H가 0일때와 0이 아닐때로 나뉨
        if (H !==0){
            console.log(H-1,60+M-45); //H가 0이 아니고 M이 45미만임으로 H에 -1해주고, M에 60분을 더해 45분을 빼줌.
            //예를 들어 H=10,M=10이면, H -1 해서 H=9, M=60+10-45=25 으로 출력함
        } else if( H === 0){ // H이가 0이면,출력값 H는 23으로 고정, M값만 계산해줌.
            console.log(23, 60+M-45);
        }
    }
}
```
* 시간 조건이 (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 임을 if문에서 고려하지 않고 코드를 짤 수 있음.

## 2022.08.11
## 2525번 오븐 시계
### 문제
    * 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.
    * 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다. 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다. 
    * 첫째 줄에 종료되는 시각의 시와 분을 공백을 사이에 두고 출력한다. (단, 시는 0부터 23까지의 정수, 분은 0부터 59까지의 정수이다. 디지털 시계는 23시 59분에서 1분이 지나면 0시 0분이 된다.)
### 풀이
```javascript
//입력값이 [14 30\n20] 이기 때문에 첫 줄과 두번째 줄을 \n으로 나누고 첫 번째주를 다시 띄어쓰기로 나눈다
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split("\n");
const times = inputData[0].split(" ");
const cookingTimes = parseInt(inputData[1]);
const H = parseInt(times[0]);
const M = parseInt(times[1]);

solution(H,M,cookingTimes);


function solution(H,M,cookingTimes){
    const result = H*60+M+cookingTimes ; //현재 시각과 걸리는 시간을 더해 분단위로 나타냄.
    const resultH = Math.floor(result/60); //분단위 시각을 60으로 나눠 내림하여 시를 나타냄.
    const resultM = result%60;// 분단위 시각을 60을 나눈 나머지로 분을 나타냄.
    if (resultH >= 24){ // 만약 resultH가 24시간이 넘어가면 -24시간을 해주어 24시가 초과되는 시간을 방지함.
        console.log(resultH-24,resultM);
    }else
    console.log(resultH,resultM);

}
```

### 삽질
```javascript

solution(H,M,cookingTimes);

function solution(H,M,cookingTimes){
    if (M+cookingTimes >= 60){
    console.log(H+1,M+cookingTimes-60);
    } else if(M+cookingTimes < 60) {
        console.log(H,M+cookingTimes);
    }
}
```
cookingTimes가 120분이 넘어가면 H+2를 해야줘야되는데 생각 못함.
너무 단순하게 생각함.

## 2480번
### 문제
    * 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다. 

    같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
    같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
    모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
    예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

    3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
    * 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다. 
    * 첫째 줄에 게임의 상금을 출력 한다.

### 풀이
```javascript
const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" "); //띄어쓰기로 나누기

let ABC = [parseInt(inputData[0]),parseInt(inputData[1]),parseInt(inputData[2])];
ABC.sort(); //sort로 오름차순으로 정렬! 


const A = ABC[0];
const B = ABC[1];
const C = ABC[2];

if (A == B && B ==C){ // 세 숫자가 같으면
    result1 = 10000+A*1000
    console.log(result1);
} else if (A===B || B ===C ){ // 정렬을 해놨기 때문에 경우의 수가 두가지. 
    if (A ===B){
        console.log(1000+A*100);
    } else if( B ===C ){
        console.log(1000+B*100);
    }
} else if(A !== B && B !== C){ //세 숫자가 각기 다르면
    console.log(C*100); //정렬을 통해 C가 젤 큰 숫자 임으로 C*100
}
```
먼저 sort를 이용해 정렬한 후 if문으로 조건을 나눈다.

### 아쉬운 점
    * let ABC = [parseInt(inputData[0]),parseInt(inputData[1]),parseInt(inputData[2])];
    이 부분을 더욱 간단하게 만들고 싶은데 +사용하는 법 말고 parseInt로 묶는 방법이 있는지 모르겠다.
    * return을 배웠는데 어떻게 활용해야 하는지 모르겠다. return에 대해 더 공부할 것.
    * 처음에 "A==B==C" 말도 안되는 조건을 완성해놓고 왜 안되는지 한참을 헤맸다. AND, OR 연산자를 공부해놓고... 거기서 헤매다니.. 나중에 고치고 나서 벙쩌있었다. 잊지 말자!

