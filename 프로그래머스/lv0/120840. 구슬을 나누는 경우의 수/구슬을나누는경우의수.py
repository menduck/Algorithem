# ball C share

import math
def solution(balls, share):
    return math.factorial(balls)/(math.factorial(share)*math.factorial(balls-share))

# 다른 사람 풀이

# soltuion2
import math

def solution(balls, share):
    return math.comb(balls, share)

# soltuion3
def solution(balls, share):
    answer = factorial(balls) / (factorial(balls - share) * factorial(share))
    return answer

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result