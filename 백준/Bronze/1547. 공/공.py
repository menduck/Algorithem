import sys
M = int(sys.stdin.readline().strip())
line = [1,2,3]

for _ in range(M):
    x,y = map(int,sys.stdin.readline().strip().split() )
    for cup_num in range(len(line)): # 0 1 2
        if  line[cup_num]== x: 
            line[cup_num] = y
        elif line[cup_num]== y: 
            line[cup_num] = x

print(line[0])