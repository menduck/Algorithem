import sys

t = int(sys.stdin.readline().strip())
vote_list = []
for _ in range(t):
  vote_list.append(int(sys.stdin.readline().strip()))

if vote_list.count(0) > vote_list.count(1) :
  print('Junhee is not cute!')
else:
  print('Junhee is cute!')