import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
  m,n = map(int, sys.stdin.readline().strip().split())
  matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
  # [[1, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0]]

  # 행과 열을 바꿈 
  new_matrix = list(zip(*matrix))
  
  cnt = 0
  for i in range(n):
    floor = m-1 # 바닥면 설정
    for j in range(m-1,-1,-1): # 뒤에서 부터 
      if new_matrix[i][j] == 1:
        cnt += floor -j
        floor -= 1
  print(cnt)