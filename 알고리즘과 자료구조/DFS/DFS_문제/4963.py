# 4963 섬의 개수

'''
# 문제 풀이
- 입력받은 행렬 요소가 순회를 통해 1인 값을 찾고 카운트해준다. 
- 그리고 그 요소를 dfs함수로 행렬 요소가 1인값을 탐색한다.
  - 먼저 매개변수로 받은 값을 0으로 값을 업데이트한다.
    - 이유: 그 다음 순회에서 다시 중복해서 탐색하지 않기 위해서
  - 상하좌우+대각선의 요소들을 탐색한다.
    - 상하좌우+대각선이 1이면 그 해당 요소의 상하좌우+대각선 요소를 탐색한다.
- 카운트 값을 출력한다.

'''
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