
# solution - 실패/시간초과
def solution(n, left, right):
    # n*n 배열 생성
    grid = [[n]*n for _ in range(n)]
    
    while n > 0:
        for i in range(n):
            for j in range(n):
                grid[i][j] = n
        n -= 1
    result = sum(grid,[])
    return result[left:right+1]

# solution - 실패/시간초과
def solution(n, left, right):
    result = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            result.append(max(i,j))
    return result[left:right+1]

# solution - 성공
import math
def solution(n, left, right):
    result= []
    for i in range(left+1,right+2):
        x = math.ceil(i/n) 
        y = (i%n if i%n else n)
        result.append(max(x,y))
    return result

# (1,1) = 1 (1,2) = 2 (1,3) = 3 (1,4) = 4
# (2,1) = 2 (2,2) = 2 (2,3) = 3 (2,4) = 4
# (3,1) = 3 (3,2) = 3 (3,3) = 3 (3,4) = 4
# (4,1) = 4 (4,2) = 4 (4,3) = 4 (4,4) = 4


solution(3,2,5)
'''
# 실패 원인
- n의 범위가 10^7까지 있기 때문에 2차원의 배열을 이중 for문으로 만들면 10^14라 범위가 큼
- left와 right의 범위 값이 10^5임으로 이를 이용해 문제를 풀어야 함.
- left와 right 사이의 값만 만들고 출력해야 시간초과가 나지 않음
'''


