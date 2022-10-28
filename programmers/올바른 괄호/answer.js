const s = "(()())"

let strS = s.split('');

for(let i =0;i<strS.length-1;i++){
  if(strS[i]+strS[i+1] === '()'){
    strS.splice(i,2);
    i--
  }
} 