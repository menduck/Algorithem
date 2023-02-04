'''
# 문제
- n개의 숫자들의 최소 공배수를 구해라

# 문제 풀이
- n개의 숫자들의 최댓값부터 모두 더한 값까지 순회한다.
- arr 요소들들로 나눴을때 0으로 떨어지면 최소공배수임으로
- 떨어지면 순회를 멈추고 값을 출력한다.

# solution - 시도/ case 1/10 시간초과
def solution(arr):
    max_common_multiple = 1
    blank = [0]*len(arr) [0,0,0,0]
    for num in arr:
        max_common_multiple *= num
    for i in range(max(arr),max_common_multiple+1): 
        if list(map(lambda x:i%x,arr)) == blank: 
            return i
            break

# 문제풀이
- 맨 처음 두 개의 요소를 유클리드 호제법으로 최소 공배수를 계산한다.
- 계산한 최소 공배수와 세 번째 요소의 최소 공배수를 구한다.
- 마지막 요소까지 반복하여 최소 공배수를 구한다.
'''

# solution - 유클리드 호제법
def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1%num2)

def lcm(num1,num2):
    return num1*num2 / gcd(num1,num2)

def solution(arr):
    result_lcm = arr[0]
    for i in range(1,len(arr)):
        result_lcm = lcm(result_lcm,arr[i])
    return result_lcm

'''
## 알게된 점.

### 유클리드 호제법
- 유클리드 호제법의 기본 전제는 num1>num2이다.
- 하지만 정렬하지 않았는데도 num1<num2에서 정상적으로 코드가 실행되는 이유는
- 코드 과정중 num1%num2를 계산할때 num1<num2임으로 값이 num1이 되고 다시 gcd(num2,num1)로 실행되기 때문이다.

### math라이브러리 이용
- math라이브러리에 이미 유클리드 알고리즘을 구현하여 최대공약수를 구하는 gcd 모듈이 있다.

```py
import math

def lcm(a,b)
    return a*b / math.gcd(a,b)
```

'''
