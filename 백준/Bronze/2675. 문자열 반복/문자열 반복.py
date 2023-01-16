import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
  R,str = sys.stdin.readline().strip().split()
  result = ''
  for s in str:
    result += s*int(R)
  print(result)