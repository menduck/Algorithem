function solution(s) {
  let zero = 0;
  let cnt = 0;
  while(s != '1') {
      let onlyOne = s.split('').filter((v) => v != 0).length
      zero += s.length - onlyOne
      s = onlyOne.toString(2)  
      cnt++
  }   
  return [cnt,zero]
}