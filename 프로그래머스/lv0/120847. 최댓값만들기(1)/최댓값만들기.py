# 문제접근
# 오름차순으로 정렬 후 가장 큰 수 두개를 곱해 반환한다.

def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]