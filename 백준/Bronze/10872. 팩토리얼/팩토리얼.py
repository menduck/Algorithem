
import sys
N = int(sys.stdin.readline().strip())
if N == 0:
  print(1)
else:
  result = 1
  for num in range(1,N+1):
    result *= num
  print(result)