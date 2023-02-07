import sys
n = int(sys.stdin.readline().strip())
bar_numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

cnt = 0
min = bar_numbers[-1]
for i in range(n-2,-1,-1):
    if bar_numbers[i] > min:
          min = bar_numbers[i]
          cnt +=1
print(cnt+1)