import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
  N = int(sys.stdin.readline().strip())
  numbers = map(int,sys.stdin.readline().strip().split())
  print(sum(numbers))