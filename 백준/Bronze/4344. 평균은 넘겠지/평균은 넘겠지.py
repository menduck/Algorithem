import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
  data = list(map(int, sys.stdin.readline().strip().split()))
  N = data[0]
  score_list = data[1:]
  
  mean_score = sum(score_list)/N
  cnt = 0
  for score in score_list:
    if score > mean_score :
      cnt += 1

  print(f'{cnt/N :.3%}')