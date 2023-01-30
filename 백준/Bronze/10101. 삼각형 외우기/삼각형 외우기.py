import sys
angles = [int(sys.stdin.readline().strip()) for _ in range(3)]
unique_angles = set(angles)

if unique_angles == {60}:
  print('Equilateral')
elif sum(angles) == 180 and len(unique_angles) == 2:
  print('Isosceles')
elif sum(angles) == 180 and len(unique_angles) == 3:
  print('Scalene')
else:
  print('Error')