import sys
N = int(sys.stdin.readline().strip())
for _ in range(N):
  score = list(map(int,sys.stdin.readline().strip().split() ))
  sort_socre = sorted(score)
  if sort_socre[-2] - sort_socre[1] >= 4:
    print('KIN')
  else:
    print(sum(sort_socre[1:-1]))