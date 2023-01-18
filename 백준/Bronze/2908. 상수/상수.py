import sys
x,y =  sys.stdin.readline().strip().split()

print(max(int(x[::-1]),int(y[::-1])))