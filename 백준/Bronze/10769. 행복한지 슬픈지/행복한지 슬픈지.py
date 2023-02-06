import sys

data = sys.stdin.readline().strip()

sad_count = data.count(':-(')
happy_count = data.count(':-)')

if sad_count == 0 and happy_count == 0:
  print('none')
elif sad_count == happy_count:
  print('unsure')
elif sad_count > happy_count:
  print('sad')
elif sad_count < happy_count:
  print('happy')