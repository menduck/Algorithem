# 문제접근
# filter를 활용하여 array의 요소를 하나씩 순회하면서 n과 같은 요소만 남기고, 그 개수를 반환한다.

# soltuion - 성공
def solution(array, n):
    return len(list(filter(lambda x: x == n, array)))

# 다른 방법

# solution -  count 사용
def solution(array, n):
    return array.count(n)

# solution - for문과 sum사용
def solution(array, n):
    return sum(1 for x in array if x == n)