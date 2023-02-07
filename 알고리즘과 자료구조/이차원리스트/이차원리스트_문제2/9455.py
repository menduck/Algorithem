# 9455 박스
'''
# 문제 풀이
- 편하게 탐색하기 위해 행렬의 열과 행을 바꾼다.
- 바닥면이 맨 오른쪽 열임으로 뒤에서부터 탐색한다.
  - 바닥면은 m-1
- 요소가 1이면
  - 바닥면이 1칸 왼쪽으로 이동 (인덱스 입장에선 -1)
  - 횟수를 세줌(바닥면에서 현재 위치값을 빼줌)
'''
import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
  m,n = map(int, sys.stdin.readline().strip().split())
  matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
  # [[1, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0]]

  # 행과 열을 바꿈 
  new_matrix = list(zip(*matrix))
  # print(new_matrix) # [(1, 0, 1, 0, 1), (0, 0, 0, 1, 0), (0, 1, 0, 0, 1), (0, 0, 1, 0, 0)]


  cnt = 0
  for i in range(n):
    # floor는 각 행마다 초기화
    floor = m-1 # 바닥면 설정
    for j in range(m-1,-1,-1): # 뒤에서 부터 
      if new_matrix[i][j] == 1:
        cnt += floor -j
        floor -= 1
  print(cnt)

