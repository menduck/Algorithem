import sys
K = int(sys.stdin.readline().strip())
result = []
for _ in range(K):
  number = int(sys.stdin.readline().strip())
  if number == 0:
    result.pop()
  else:
    result.append(number)
print(sum(result))