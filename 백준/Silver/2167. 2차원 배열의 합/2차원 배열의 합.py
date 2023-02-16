import sys
n,m = map(int,sys.stdin.readline().strip().split())
matrix = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

k = int(sys.stdin.readline().strip())
for _ in range(k):
    i,j,x,y = map(int,sys.stdin.readline().strip().split())
    matrix_sum = 0
    for a in range(i-1,x):
        for b in range(j-1,y):
            matrix_sum += matrix[a][b]
    print(matrix_sum)