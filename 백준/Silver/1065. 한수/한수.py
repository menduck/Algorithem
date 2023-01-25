import sys
def arithmetic_sequence(N) :
  cnt = 0
  for i in range(1, N+1) :
    numbers = list(map(int, str(i)))
    if i < 100:
      cnt += 1
    elif numbers[0] - numbers[1] == numbers[1] - numbers[2] :
      cnt +=1
  print(cnt)

N = int(sys.stdin.readline().strip())
arithmetic_sequence(N)