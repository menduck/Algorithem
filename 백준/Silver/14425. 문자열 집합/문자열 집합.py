import sys
N, M = map(int, sys.stdin.readline().strip().split())
S = set([sys.stdin.readline().strip() for _ in range(N)])
check_str = [sys.stdin.readline().strip() for _ in range(M)]
cnt = 0
for word in check_str:
  if word in S: # O(1)
    cnt +=1
print(cnt)