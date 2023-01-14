import sys
_, X = map(int, sys.stdin.readline().strip().split())
A_list = list(map(int, sys.stdin.readline().strip().split()))

result = []
for num in A_list :
  if num < X :
    result.append(num)
print(*result)