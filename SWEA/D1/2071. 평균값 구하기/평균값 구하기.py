t = int(input())
for i in range(t) :
  numbers = list(map(int, input().split()))
  mean = round(sum(numbers) / 10)
  print(f'#{i+1} {mean}')