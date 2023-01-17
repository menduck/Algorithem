import sys
str = (sys.stdin.readline().strip()).upper()
result = {}
for w in list(set(str)):
  result[w] = str.count(w)
max_key = [k for k,v in result.items() if max(result.values()) == v]
if len(max_key) > 1:
  print('?')
else:
  print(max_key[0])