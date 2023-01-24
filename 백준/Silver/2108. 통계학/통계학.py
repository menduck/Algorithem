import sys
from collections import Counter
N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
sort_numbers = sorted(numbers)

print(round(sum(numbers)/N))
print(sort_numbers[N//2])

common_list = Counter(sort_numbers).most_common()


if len(common_list) > 1 and common_list[0][1] == common_list[1][1]:
    print(common_list[1][0])
else:
    print(common_list[0][0])

print(max(sort_numbers) - min(sort_numbers))