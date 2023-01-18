import sys
N = int(sys.stdin.readline().strip())
number_list = []
for _ in range(N):
  num = int(sys.stdin.readline().strip())
  number_list.append(num)

print(*sorted(number_list), sep = '\n')