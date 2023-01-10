# - 주어진 10개의 수 중 가장 큰 수를 출력한다.
t = int(input())
for i in range(t) :
  numbers = list(map(int, input().split()))
  print(f'#{i+1} {max(numbers)}')