// 다른 코드 풀이
const solution = (arr) => {
  let zeroCount = 0;
  let oneCount = 0;

  // 쪼개는 함수 (시작행, 시작열, 비교할 길이)
  // 시작하는 첫 번째 요소와 다른 값들이 같으면 true, 다르면 false
  const divide = (row, col, n) => {
      let canDivide = true;

      for (let y=row; y < row+n; y++) {
          for (let x=col; x < col+n; x++) {
              if (arr[row][col] !== arr[y][x])
                  canDivide = false;
          }
      };
      //모두 같은 값이 아니면, 4분할하여 다시 쪼갠다.(재귀호출)
      if (!canDivide) {
          const halfN = parseInt(n/2);
          divide(row, col, halfN)
          divide(row, col+halfN, halfN)
          divide(row+halfN, col, halfN)
          divide(row+halfN, col+halfN, halfN)
      // 모두 같은 값이면, 첫 번째 요소의 값으로 카운팅해준다.
      } else {
          if (arr[row][col]) oneCount += 1;
          else zeroCount += 1;
      }
  }
  const N = arr.length;
  divide(0, 0, N);
  return [zeroCount, oneCount];    
}

// 실패 - 재귀 구현 실패
function solution1(arr) {
  let len = arr.length
  let sum = 0
  let totalCount = [0,0]
  let tep = arr
  let a = [[],[],[],[]]
  while(len > 2 ){
    console.log(tep,len)
    tep.forEach((v,idx) => {
      v.forEach((v2, idx2) => {
        if (idx < (len/2) && idx2 < (len/2)){
          a[0].push(v2)
        }
        else if (idx < (len/2) && idx2 >= (len/2)){
          a[1].push(v2)
        }
        else if (idx >= (len/2) && idx2 < (len/2)){
          a[2].push(v2)
        }
        else if (idx >= (len/2) && idx2 >= (len/2)){
          a[3].push(v2)
        }
      })
    })
    a.map((v) =>{
      if (new Set(v).size === 1) {
        if (v[0] === 0){
          return totalCount[0] += 1
        } else{
          return totalCount[1] += 1
        }
      } else if(len === 4) {
        v.forEach((ele) => {
          if (ele === 0) return totalCount[0] += 1
          return totalCount[1] += 1
        })
      }
    })
    tep = a.filter((v) => new Set(v).size !== 1)
    console.log('*************')
    console.log(tep,len,'요로')
    len /=  2
    a = [[],[],[],[]]
  }
  console.log(totalCount)
  return totalCount
}

// solution(	[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
solution(	[[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])

