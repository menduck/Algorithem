# 1110 더하기 사이클

import sys
N = sys.stdin.readline().strip() # '26'

result = N # 26
cnt = 0


while True:
  N_list = list(map(int,N)) # [2,6] int
  N_sum_last = str(sum(N_list))[-1] # '8'
  N = str(N_list[-1]*10 + int(N_sum_last)) # '68'
  cnt += 1
  if N == result:
    print(cnt)
    break