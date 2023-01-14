import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
  OX_str = sys.stdin.readline().strip().split('X')
  
  sum = 0
  for O_list in OX_str:
    sum += (len(O_list)*(1+len(O_list)))/2
  print(int(sum))