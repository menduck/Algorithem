import sys
case_num = int(sys.stdin.readline()) 
for _ in range(case_num) :
  x,y = map(int, sys.stdin.readline().strip().split(' '))
  print(x+y)