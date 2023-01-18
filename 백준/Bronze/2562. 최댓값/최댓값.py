import sys

number_list = [int(sys.stdin.readline().strip()) for _ in range(9)]
max_num = max(number_list)
print(max_num)
print(number_list.index(max_num)+1)