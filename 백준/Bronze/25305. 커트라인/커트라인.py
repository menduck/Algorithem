import sys
N,k = map(int, (sys.stdin.readline().strip().split()))
score = map(int, (sys.stdin.readline().strip().split()))
sort_score = sorted(score, reverse= True)
print(sort_score[k-1])