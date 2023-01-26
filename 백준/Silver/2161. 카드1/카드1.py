import sys
N = int(sys.stdin.readline().strip())
card_list = [num for num in range(1,N+1)]

while len(card_list) > 1:
  print(card_list.pop(0), end = ' ')
  card_list.append(card_list.pop(0))
print(*card_list)