 
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

