import sys

data = [list(sys.stdin.readline().strip()) for _ in range(5)]

for i in range(15): 
    for j in range(5):
        if len(data[j]) > i : 
            print(data[j][i], end ='')