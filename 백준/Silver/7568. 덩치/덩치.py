import sys
n = int(sys.stdin.readline().strip())
data =[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)] 
for i in data:
    ranking = len(list(filter(lambda x: x[0]>i[0] and x[1]>i[1],data))) +1
    print(ranking)