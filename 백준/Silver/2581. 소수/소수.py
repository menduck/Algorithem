import sys
M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
numbers = []
for num in range(M,N+1): # 60,100
  result = [num for n in range(1,num+1) if num % n == 0]
  if len(result) == 2:
    numbers.append(num)
if len(numbers) == 0:
  print(-1)
else:
  print(sum(numbers))
  print(min(numbers))
    