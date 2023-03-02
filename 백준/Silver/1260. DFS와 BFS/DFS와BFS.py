import sys
from collections import deque

# 가장 최근에 발견되고 아직 체크되지 않은 간선을 가진 정점 v로 부터 나온 간선을 조사하고 v의 모든 간선이 조사되면 v가 발견된 최초의 정점으로 다시 돌아가서 그 정점으로부터 나오는 간선들을 조사한다.
def dfs(graph,visted,start):
    # 방문 체크
    visted[start] = True

    # 방문한 정점 출력
    print(start,end=' ')

    # 재귀
    for i in graph[start]:
        if not visted[i]:
            dfs(graph,visted,i)

# 최단 경로/가장 앞에 있는 정점과 그 정점에 인접한 노트를 탐색
def bfs(graph,visted,start):
    queue = deque([start])

    # 방문 체크
    visted[start] = True

    # queue가 빈 배열일때까지 반복
    while queue:
        # 가장 오래된 요소를 v에 저장하고 출력함
        q_v = queue.popleft()
        print(q_v,end = ' ')

        for i in graph[q_v]:
            if not visted[i]:
                queue.append(i)
                # 방문 체크
                visted[i] = True

m,n,v = map(int, sys.stdin.readline().strip().split())

# 인접 리스트 생성
graph = [[] for _ in range(m+1)]
for _ in range(n):
    v1,v2 = map(int, sys.stdin.readline().strip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 정점 번호가 작은 것을 먼저 방문하기 위해 정렬
for v_list in graph:
    v_list.sort()

visted_dfs = [False]*(m+1)
visted_bfs = [False]*(m+1)

dfs(graph,visted_dfs,v)
print()
bfs(graph,visted_bfs,v)

