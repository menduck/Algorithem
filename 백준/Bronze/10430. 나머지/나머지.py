import sys
a,b,c = map(int, sys.stdin.readline().strip().split(' '))
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)