import sys
N,M = map(int, sys.stdin.readline().strip().split())
one_matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
two_matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for i in range(N):
  result = []
  for j in range(M):
    result.append(one_matrix[i][j] + two_matrix[i][j])
  print(*result,sep= ' ')