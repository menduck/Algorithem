import sys
data = [[0]*8 for _ in range(8)]

cnt = 0

for i in range(8):
    room = sys.stdin.readline().strip()
    for j in range(len(room)):
        if i%2 == 0 and j%2 == 0 and room[j] == 'F':
          cnt += 1
        elif i%2 == 1 and j%2 == 1 and room[j] == 'F':
          cnt += 1      
print(cnt)