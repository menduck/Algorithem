/**
 * 문제접근
 *  n = 1부터 +1씩 증가하면서 몇 가지 방법이 있는지 계산한다.
 * ===============================================
 * n = 1, result = 1
 * n = 2, result = 2
 * n = 3, result = 3
 * n = 4, result = 5
 * n = 5, result = 8
 * n이 증가함에따라 result가 피보나치수열을 따른다는 것을 확인할 수 있다.
 * 문제는 피보나치수열을 구현하면 됨. 
 * */ 


function solution(n) { 
	const result = [1,2]; 
    for (let i = 0; i < n-2; i++) { 
      const a = result[i]; 
      const b = result[i + 1]; 
      result.push((a + b) % 1000000007); 
    } 
    return result[n-1]; 
}
