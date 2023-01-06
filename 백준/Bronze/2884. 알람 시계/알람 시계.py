import sys
hour, min = map(int, sys.stdin.readline().strip().split(' '))

min_45ago = min - 45

if min_45ago == 0:
  print(f'{hour} 0')
elif min_45ago < 0:
  if hour == 0 :
    print(f'23 {60 + min_45ago}')
  else:
    print(f'{hour - 1} {60 + min_45ago}')
else :
  print(f'{hour} {min_45ago}')