import sys
score = [int(sys.stdin.readline()) for _ in range(10)]
result = {}
for i in range(10,-1,-1):
    score_sum = sum(score[:i])
    result[score_sum] = abs(100 -score_sum)
sort_result = sorted(result.items(), key = lambda x:(x[1],-x[0]) )
print(sort_result[0][0])