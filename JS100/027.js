const input = "Yujin Hyewon" +"\n" + "70 100"
const inputName = input.split('\n')[0].split(' ');
const score = input.split('\n')[1].split(' ');


const result = inputName.reduce((acc,cur,idx)=>{
  acc[cur] = score[idx];
  return acc;
},new Object);

//reduce의 두번째 인수를 new Object를 주어 빈 객체를 만든다.
console.log(result)