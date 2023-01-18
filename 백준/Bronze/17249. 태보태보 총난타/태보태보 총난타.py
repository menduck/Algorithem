import sys
data = sys.stdin.readline().strip().split('(^0^)') # ['@===@==@=@==', '==@=@===@']
print(data[0].count('@'), data[1].count('@'))