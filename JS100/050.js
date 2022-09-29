
function bubble(arr) {
  let result = arr.slice();
  for(let i =result.length-1;i>=0;i--){ //배열 끝에서부터 좁혀온다.
    for(let j = 0; j<i; j++ ){
      if(result[j]>result[j+1]){ //왼쪽 요소가 오른쪽요소보다 크면
        // 왼쪽요소와 오른쪽 요소 자리를 바꾼다.
        let temp = result[j]; // 왼쪽 요소를 temp에 잠시 넣어 놓고
        result[j] = result[j+1]; // 왼쪽 요소의 값을 오른쪽 요소의 값으로 설정!
        result[j+1] = temp; // 오른쪽 요소의 값은 temp 값으로 저장한다.
        
      } // 이 과정을 배열의 크기 -1 만큼 반복한다.
    } 
  } return result
}


const input = "4 2 3 8 5"
const items = input.split(' ').map((n) => {
  return parseInt(n, 10);
}); [4,2,3,8,5]


console.log(bubble(items));

