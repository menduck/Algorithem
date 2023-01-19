import sys
numbers = []
for _ in range(7):
  number = int(sys.stdin.readline().strip())
  if number% 2:
    numbers.append(number)

  
if len(numbers) :
  print(sum(numbers))
  print(min(numbers))
else:
  print(-1)