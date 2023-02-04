# 예상대진표

# 내풀이
# 1. 범위를 반씩 나눠 a,b가 있는지 확인한다.
# 2. 양쪽에 a,b가 있으면 그 경기는 끝까지 진행하기 때문에 2의 지수를 구한다.
# 3. 한쪽에 a,b가 있으면 다시 1번 2번 과정을 반복한다. (양쪽에 a,b가 존재할때까지)


# solution - 시도/성공
# 2제곱수의 지수를 반환하는 함수
def exponent_two(number): 
    cnt = 0
    while number >1:
        number = number/2
        cnt += 1
    return cnt

def solution(n,a,b):
    while n > 1: # 4
        # 범위에 반을 나누어 a와 b가 각각 있으면 경기는 2제곱수의 지수만큼 진행한다.
        half_stage = n/2 + 0.5 
        if (a < half_stage and half_stage< b) or (b < half_stage and half_stage< a) :
            return exponent_two(n) #1
        
        # 만약 범위 한쪽에 a,b가 있다면 a,b는 다시 1번부터 시작하여 값을 수정한다.
        else:
            a =  a - n/2 if a - n/2 > 0 else a
            b =  b - n/2 if b - n/2 > 0 else b
            n = n/2

# 코드 리뷰
'''
- 2제곱수의 지수를 반환하는 함수를 만들지 않고 로그로 나타내면 됨.
- 반을 확인할때 0.5를 더하는 것이 아니라 2로 나눠 몫으로 확인하면 됨.
'''

# soltuion - 보완한 코드/성공
import math

def solution(n,a,b):
    while n > 1: # 4
        # 범위에 반을 나누어 a와 b가 각각 있으면 경기는 2제곱수의 지수만큼 진행한다.
        if math.ceil(a/(n/2)) != math.ceil(b/(n/2)):
            return int(math.log(n,2))
        
        # 만약 범위 한쪽에 a,b가 있다면 a,b는 다시 1번부터 시작하여 값을 수정한다.
        else:
            a =  a - n/2 if a - n/2 > 0 else a
            b =  b - n/2 if b - n/2 > 0 else b
            n = n/2
print(solution(8,4,7))


# 다른사람 풀이
def solution(n,a,b):
    answer = 0
    while a != b: # 라운드 번호가 같으면 반복문을 빠져나간다.
        answer += 1
        a, b = (a+1)//2, (b+1)//2 # a,b를 라운드번호로 재할당한다.

    return answer
