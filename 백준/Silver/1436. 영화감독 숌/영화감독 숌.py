import sys
n = int(sys.stdin.readline().strip())

target_number = 666

while n:
    if '666' in str(target_number):
        n -= 1
    target_number += 1
print(target_number-1)