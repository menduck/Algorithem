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