import sys

test_cases = sys.stdin.readlines()

for test_case in test_cases :
  A,B = map(int, test_case.split())
  print(A+B)