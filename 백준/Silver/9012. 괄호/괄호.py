import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
  data = sys.stdin.readline().strip()
  stack = []

  for bracket in data:
    if len(stack) == 0 :
      stack.append(bracket) 
    elif stack[-1] == '(' and bracket == ')':
      stack.pop()
    else:
      stack.append(bracket) 
  
  if len(stack) == 0:
    print('YES')
  else:
    print('NO')