 
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
    <img src="img/2588.png" width = "300" height = "300">
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
