# 4963 섬의 개수

import sys
# 무한 재귀호출을 방지
sys.setrecursionlimit(10000)

def dfs(x,y):
    # 상하좌우대각선 탐색
    dx = [-1,-1,-1,0,0,1,1,1]
    dy = [-1,0,1,-1,1,1,0,-1]

    # 탐색한 요소는 0으로 초기화함.
    # 이걸 해줘야 i,j에서 이미 카운트한 요소들을 다시 탐색하지 않음
    field[x][y] = 0

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        # 경계면이 아니고 주위가 1이면
        if 0<=nx<n and 0<=ny<m and field[nx][ny] == 1:
            # 다시 그 요소를 탐색함.
            dfs(nx,ny)

while True:
    m,n = map(int, sys.stdin.readline().strip().split())

    # 0 0 이 입력되면 입력받는 것을 멈춘다.
    if n+m == 0:
        break
    
    count = 0
    field = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                  dfs(i,j)
                  count += 1        

    print(count)