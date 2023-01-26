import sys
T = int(sys.stdin.readline().strip())
coin_unit = [25,10,5,1]
for _ in range(T):
  coin_count = []
  changes = int(sys.stdin.readline().strip())
  while changes > 0:
    for coin in coin_unit:
      coin_count.append(changes//coin)
      changes = changes%coin
  print(*coin_count)