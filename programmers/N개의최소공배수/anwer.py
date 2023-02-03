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
    blank = [0]*len(arr)
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