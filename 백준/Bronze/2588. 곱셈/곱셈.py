import sys 
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

for n in b[::-1]: # 일의 자리부터 곱해야 하므로 b를 뒤집어서 차례대로 곱한다.
  print(int(a) * int(n)) # 472 * 5 / 472 * 8 /472 * 3
print(int(a) * int(b)) # 472*385