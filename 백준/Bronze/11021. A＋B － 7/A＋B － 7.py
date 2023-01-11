import sys
t = int(sys.stdin.readline().strip())
for test_count in range(1,t+1) :
  a, b = map(int, sys.stdin.readline().strip().split())
  print(f'Case #{test_count}: {a+b}')