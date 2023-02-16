import sys
document = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()

print(len(document.split(target))-1)