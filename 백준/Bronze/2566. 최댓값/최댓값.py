import sys
matrix = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(9)]
max_number = 0
row = 1
column = 1
for i in range(9):
  for j in range(9):
    if max_number < matrix[i][j]:
      max_number = matrix[i][j]
      row = i+1
      column = j+1
print(max_number)
print(row, column)
