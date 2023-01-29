import sys
N = int(sys.stdin.readline().strip())
start = 1
cnt = 1
while N > start:
    start += 6*cnt
    cnt+= 1
print(cnt)