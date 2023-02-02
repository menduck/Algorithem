import sys
N = int(sys.stdin.readline().strip())
pi = list(map(int,sys.stdin.readline().strip().split()))

# 오르막의 크기
d =[pi[i+1] - pi[i] for i in range(len(pi)-1)]

total_list = []
total = 0
for j in range(len(d)):
    if d[j] > 0:
        total += d[j]
    else:
        total = 0
    total_list.append(total)

if total_list == [0]*len(d):
    print(0) 
else:
    print(max(total_list))