import sys
t = int(sys.stdin.readline().strip())

number_list = list(map(int, sys.stdin.readline().strip().split()))
max_number = max(number_list)

new_number_list = list(map(lambda x : x/max_number, number_list))

print(sum(new_number_list)/t*100)