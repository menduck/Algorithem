import sys
import math
A,B,C = map(int, sys.stdin.readline().strip().split())

if B>= C:
  print(-1)
else:
  print(math.floor(A/(C-B)+1))