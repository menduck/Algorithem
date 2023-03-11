'''
# 문제 접근
- 각 작업일을 계산한다.
- deque을 활용하여 조건에 따라 몇 개의 기능이 배포되는지 카운팅한다.
'''

import math
from collections import deque
def solution(progresses, speeds):
    days = [math.ceil((100-p)/s)for p,s in zip(progresses,speeds)]

    d_days = deque(days)
    count = 1
    result = []

    day = d_days.popleft()

    while d_days:
        # 이전 기능의 배포가 완성된 상태가 아닐때, 카운팅함.
        if day>=d_days[0]:
            d_days.popleft()
            count+=1
        # 완성된 상태라면 기준 day를 재할당하고 다시 카운팅 한다.
        else:
            day = d_days.popleft()
            result.append(count)
            count = 1
    result.append(count)
    return result
        

# 다른 사람 풀이

# 접근방법
'''
파이썬에서 음수 값을 몫 나누기 연산자(//)를 이용해 나누면, 
나누기 결과보다 작은 정수 중 가장 큰 정수를 돌려준다.

print(-10 / 3)   => -3
print(-10 // 3)  => -4
'''

def solution(progresses, speeds):
    deployed_service = []
    for i in range(len(progresses)):
        day = - ((progresses[i] - 100) // speeds[i])
        if not deployed_service or deployed_service[-1][0] < day:
            deployed_service.append([day, 1])
        else:
            deployed_service[-1][1] += 1
    
    return [d[1] for d in deployed_service]