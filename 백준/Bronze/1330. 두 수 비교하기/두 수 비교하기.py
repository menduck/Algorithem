# 1330
import sys
a,b = map(int, sys.stdin.readline().strip().split(' '))
# A가 B보다 큰 경우에는 '>'를 출력한다.
if a > b :
  print('>')
# A가 B보다 작은 경우에는 '<'를 출력한다.
if a < b :
  print('<')
# A와 B가 같은 경우에는 '=='를 출력한다.
if a == b:
  print('==')

