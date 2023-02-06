import sys
n = int(sys.stdin.readline().strip())
connected_n = int(sys.stdin.readline().strip())

# 인접리스트 만들기
computer_grape = [[]*n for _ in range(n+1)]
for _ in range(connected_n):
    v1,v2 = map(int, sys.stdin.readline().strip().split())
    computer_grape[v1].append(v2)
    computer_grape[v2].append(v1)

# print(computer_grape) [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

visted = [False] * (n+1)

stack = [1] # 1번 컴퓨터 탐색 시작
visted[1] = True

while stack:
    cur = stack.pop()

    for adj in computer_grape[cur]:
        if not visted[adj]:
            visted[adj] = True
            stack.append(adj)


print(visted.count(True) -1) # 자기 자신은 빼야되니때문에 -1

