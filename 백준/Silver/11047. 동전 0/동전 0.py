import sys
N,K = map(int, sys.stdin.readline().strip().split())
coin_unit = [int(sys.stdin.readline().strip()) for _ in range(N)]
coin_unit.sort(reverse=True)
cnt = 0
while K > 0:
    for coin in coin_unit:
        cnt += K//coin
        K = K%coin
print(cnt)