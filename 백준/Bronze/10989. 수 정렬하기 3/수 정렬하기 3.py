import sys
N = int(sys.stdin.readline().strip())
numbers = [0] * 10001
for _ in range(N):
  numbers[int(sys.stdin.readline().strip())] += 1

for i in range(10001):
  if numbers[i] != 0:
    for _ in range(numbers[i]):
      print(i)
      