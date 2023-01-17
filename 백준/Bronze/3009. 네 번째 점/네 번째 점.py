import sys
x_list = []
y_list = []
x_y_list = []
for _ in range(3):
  x,y = map(int, sys.stdin.readline().strip().split())
  x_y_list.append([x,y])
  x_list.append(x)
  y_list.append(y)

result = []
for i in set(x_list):
  for j in set(y_list):
    result.append([i,j])

for p in result:
  if p not in x_y_list:
    print(*p)