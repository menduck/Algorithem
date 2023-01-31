import sys
from collections import Counter

numbers = [int(sys.stdin.readline().strip()) for _ in range(10)]

common_number = Counter(numbers).most_common(1)
average = sum(numbers) // 10

print(average, common_number[0][0], sep = '\n')