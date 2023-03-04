'''
# 문제 접근
- dsf로 푼다.
- 입력값들을 인접 리스트로 바꿔주고 1로 이뤄진 무리들의 개수를 출력한다.
'''

# solution - 성공

def dfs(x,y):
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    graph[x][y] = 0

    q = list()
    q.append([x,y])

    while q:
        x,y = q.pop()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
                q.append([nx,ny])
                graph[nx][ny] = 0
            
import sys
t = int(sys.stdin.readline().strip())
# 정점의 개수 = 10 < 간선의 개수 = 17 인접 행렬이 효율

for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().strip().split())

    graph = [[0]*n for _ in range(m)]

    # 인접 행렬 생성
    for _ in range(k):
        v1, v2 = map(int, sys.stdin.readline().strip().split())
        graph[v1][v2] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                count += 1
                dfs(i,j)
    
    print(count)