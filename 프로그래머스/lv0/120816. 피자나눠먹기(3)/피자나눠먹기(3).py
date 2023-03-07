# 문제 접근
# - n명이 slice 조각을 가진 피자를 최소 한 조각 이상 먹으려면 몇 판의 피자가 필요한가?
# - n을 slice에 나눈 몫을 올림하여 반환한다.

# solution - 성공
import math
def solution(slice, n):
    return math.ceil(n/slice)

# 다른 사람 풀이
def solution(slice, n):
    return ((n - 1) // slice) + 1

# math.ceil를 사용하지 않고 올림을 구현하여 문제를 풂