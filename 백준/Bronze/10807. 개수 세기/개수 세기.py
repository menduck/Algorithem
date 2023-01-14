import sys
N = int(sys.stdin.readline().strip())
data = list(sys.stdin.readline().strip().split())
target_num = sys.stdin.readline().strip()

print(data.count(target_num))