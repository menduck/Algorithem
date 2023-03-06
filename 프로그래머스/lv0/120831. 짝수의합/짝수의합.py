# 문제 풀이
# range로 n까지의 짝수를 순회하면서 새로운 변수에 누접합한다.

# solution1 - 성공
def solution(n):
    even_sum = 0
    for i in range(0,n+1,2):
        even_sum += i
    return even_sum

# solution2 - 성공
def solution(n):
    return sum(range(0, n+1, 2))

# 내장함수 sum을 활용하여 n까지의 짝수 객체인 range를 바로 다 더해 반환함.
