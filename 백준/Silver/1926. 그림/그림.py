
'''
# 문제 접근
- 그림의 개수와 그림 넓이의 최댓값을 출력해야 한다.
- dfs를 사용하여 완전탐색한다.
- 요소 하나씩 접근하여 상하좌우를 검사한다.
  - 만약 1로 이어져 있는 부분은 카운팅 해준다. => 그림의 개수
  - 1이 몇 개로 이어져 있는지 카운팅하고 반환한다. => 그림의 넓이
  - 반환 받은 그림의 넓이를 저장하여 max인 값을 찾아 출력한다.
-  

'''
# solution - 성공
import sys

def dfs(x,y):
  # 상하좌우 검사
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  
  # 중복되지 않게 검사한 요소는 0으로 초기화
  field[x][y] = 0

  # 넓이값 1로 초기화
  area = 1

  q = list()
  q.append([x, y])

  while q: # q가 빈배열이 아니면
    # x,y는 q의 제일 최근 좌표가 됨
    # 1인 요소들을 찾아 계속 탐색하게 만듦
    x,y = q.pop()
    for i in range(len(dx)):
      nx = x+dx[i]
      ny = y+dy[i]

      # 범위에 벗어나지 않고 1이면
      if 0<=nx<n and 0<=ny<m and field[nx][ny] == 1:
        # q에 좌표를 저장하고 중복 검사되지 않기 위해 0으로 초기화
        q.append([nx,ny])
        field[nx][ny] = 0

        # 넓이를 카운팅함
        area += 1

  # 빈 배열이면 넓이를 반환함
  return area
  
n, m = map(int, sys.stdin.readline().strip().split())

# 도화지 저장
field = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
# field = [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

count = 0
painting_area = 0

# 도화지 요소 하나씩 검사
for i in range(n):
  for j in range(m):
    if field[i][j] == 1:
      # 그림의 개수를 카운팅 함.
      count += 1
      # 가장 큰 넒이 값을 저장함
      painting_area = max(dfs(i,j), painting_area)
      
print(count)
print(painting_area)