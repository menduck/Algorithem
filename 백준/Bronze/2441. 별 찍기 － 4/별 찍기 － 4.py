import sys
n = sys.stdin.readline().strip()
repeat_num = int(n)
while repeat_num > 0 :
    star = '*'*repeat_num
    print(star.rjust(int(n)))
    repeat_num -= 1