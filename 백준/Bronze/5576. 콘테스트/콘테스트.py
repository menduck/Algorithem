import sys
w_score = [int(sys.stdin.readline().strip()) for _ in range(10)]
k_score = [int(sys.stdin.readline().strip()) for _ in range(10)]

sort_w_score = sorted(w_score, reverse=True)
sort_k_score = sorted(k_score, reverse=True)
print(sum(sort_w_score[0:3]), sum(sort_k_score[0:3]))