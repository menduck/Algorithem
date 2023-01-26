import sys
N = int(sys.stdin.readline().strip())
numbers = sys.stdin.readline().strip().split()

print(len(numbers) - len(set(numbers)))