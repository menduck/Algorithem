//js001
var nums = [100, 200, 300, 400, 500];
nums.splice(3,2);
console.log(nums)

//js002
var arr = [200, 100, 300];
arr.splice(2,0,1000)
console.log(arr);

//js003
var arr1 = [100, 200, 300];
console.log(typeof(arr1));
//object
//array이지만, typeof로 나타내면 object라고 나온다.

//js004
console.log(typeof(2.22)) //number

//js005 3번 16
var a = 10;
var b = 2;

for(var i=1; i<5; i+=2){
    a += i;
}
console.log(a+b);
//i가 2씩 증가, 5 미만임으로 i=1,3 a에 누적합계된다. for문을 통과하면 a = 10+1+3 = 14, b = 2임으로 a+b = 16 이다.

//js006 2번 1
/*0, -0, null, false, NaN, undefined, 빈 문자열 ("")이라면 객체의 초기값은 false가 됩니다. 문자열 "false"를 포함한 그 외 모든 다른 값은 초기값을 true로 설정합니다.*/

//js007 
/* 3번 let은 예약어 임으로 변수명을 사용하지 못한다. 4번 숫자는 맨앞에 오지 못한다. */

//js008 84
var d = {
  'height':180,
  'weight':78,
  'weight':84,
  'temperature':36,
  'eyesight':1
};
//맨 뒤에것만 출력이 된다.
console.log(d['weight']); //84

//js009
var year = '2019';
var month = '04';
var day = '26';
var hour = '11';
var minute = '34';
var second = '27';

var result = `${year}/${month}/${day} ${hour}:${minute}:${second}`
var result2 = year.concat('/',month,'/',day,' ',hour,':', minute, ':', second);
console.log(result); //2019/04/26 11:34:27
console.log(result2); //2019/04/26 11:34:27

//js010
const input = 5;
let answer =''
for(let j=0;j<input;j++){
  for(let k =input-1;k>j;k--){
    answer += " ";
  }
  for(let m =0;m<=(j*2);m++){
    answer += "*";
  }
  answer += '\n';
};
console.log(answer)