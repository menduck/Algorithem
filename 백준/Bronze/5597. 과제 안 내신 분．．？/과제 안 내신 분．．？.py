import sys

number_list = [int(sys.stdin.readline().strip()) for _ in range(1,29)]

student = []
for i in range(30):
  if i+1 not in number_list:
    student.append(i+1)
print(*student, sep= '\n')