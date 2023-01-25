def fibonacci_number(number):
  if number <= 1:
    return number
  else:
    return fibonacci_number(number-1)+fibonacci_number(number-2)
import sys
n= int(sys.stdin.readline().strip())
print(fibonacci_number(n))