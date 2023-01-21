import sys
N = int(sys.stdin.readline().strip())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
sort_numbers = sorted(numbers)
print(*sort_numbers, sep = '\n')