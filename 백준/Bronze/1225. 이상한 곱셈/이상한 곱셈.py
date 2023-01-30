import sys
A, B =  sys.stdin.readline().split()

result = 0

print(sum(list(map(int, A)))* sum(list(map(int, B))))