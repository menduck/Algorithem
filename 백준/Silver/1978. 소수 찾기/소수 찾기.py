import sys
T = sys.stdin.readline().strip()
numbers = map(int, sys.stdin.readline().strip().split())

count = 0
for num in numbers:
  result = [num for n in range(1,num+1) if num % n == 0]
  if len(result) == 2 :
    count += 1
print(count)