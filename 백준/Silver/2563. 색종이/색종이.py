import sys

n = int(sys.stdin.readline().strip())
matrix = [[0]*100 for _ in range(100)]
for _ in range(n):
    x,y = map(int,sys.stdin.readline().strip().split())
    for x_p in range(x,10+x):
        for y_p in range(y,10+y):
            matrix[x_p][y_p] =1
print(sum(map(sum, matrix)))