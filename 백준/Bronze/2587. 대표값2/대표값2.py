import sys

numbers = [int(sys.stdin.readline().strip()) for _ in range(5)]
sort_numbers = sorted(numbers)
print(sum(sort_numbers)//5)
print(sort_numbers[2])