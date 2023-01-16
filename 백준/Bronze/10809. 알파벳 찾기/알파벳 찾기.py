import sys
str = sys.stdin.readline().strip()
alphablet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphablet :
  print(str.find(i), end = ' ')