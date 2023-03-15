# solution - 실패
def solution(n):
    result = set()
    while n > 1:
        for i in range(2,n+1):
            if n % i == 0:
                n = n//i
                result.add(i)
    return list(result)
print(solution(24))
'''
- n = 24일때, 기댓값은 [2,3] 이지만 출력값은 [2,3,4]가 나온다.
- 4는 소인수가 아니지기 때문 
'''

# solution - 성공
def solution(n):
    result = set()
    i = 2
    while n >1:
        if n % i == 0:
            n = n//i
            result.add(i)
        else:
            i += 1
    sort_result = sorted(list(result))
    return sort_result