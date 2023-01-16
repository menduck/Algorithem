import sys
N,X = map(int,sys.stdin.readline().strip().split())

num_list = map(int,sys.stdin.readline().strip().split())
for num in num_list:
  if num < X :
    print(num, end = ' ')