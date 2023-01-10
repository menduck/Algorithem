t = int(input())
for i in range(t) :
  a, b = map(int, input().split())
  quotient = a // b
  remainder = a % b
  print(f'#{i+1} {quotient} {remainder}')