function solution(word){ 
  let result = 0
  vowel = {'A' : 0, 'E' : 1, 'I' : 2, 'O' : 3, 'U': 4}

  word.split('').forEach((w,idx) => {
    const vow = vowel[w];
    result += vow * sumCount(4-idx) + 1;
  })
  return result
}

function sumCount(idx) {
  let sum = 0
  for(let i = idx; i >= 0; i--){
    sum += 5**i
  }
  return sum;
}
console.log(solution('A'))

