import sys
result_number = 1
for _ in range(3):
  result_number *= int(sys.stdin.readline().strip())

result_dict = {}
for i in range(10):
  result_dict[i] = str(result_number).count(str(i))

print(*list(result_dict.values()), sep= '\n')
