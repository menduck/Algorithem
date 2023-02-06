# 그래프 탐색 알고리즘

# DFS(깊이우선탐색)
- 시작 정점으로 갈 수 있는 하위 정점까지 가장 깊게 탐색
- 막히면 다시 돌아와서 다른 정점의 길을 탐색함
- 결국 모든 정점을 방문하는 순회 방법
- 그래프의 깊이를 우선으로 탐색하기 위해 ***스택*** 의 개념을 활용

<p align="center">
<img src = 'https://user-images.githubusercontent.com/39366835/216967296-19b0b603-d68f-4307-9736-2c7ed98d690c.PNG'>
</p>

## DFS 특징
- 모든 정점을 방문할 때 유리
- 경우의 수, 순열과 조합문제
- 너비우선탐색(BFS)에 비해 코드 구현이 간단.
  - 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우 BFS가 유리

## DFS 구현
1. 현재 정점 방문 처리
2. 인접한 모드 정점 확인
3. 방문하지 않은 인접 정점 이동

```py
grape = [[1,2],[0,3,4],[0,4,5],[1],[1,2,6],[2],[4]]
n = len(grape)
#  노드별 체크 리스트 만들기(특정 노드에 방문을 했는지 안했는지)
visted = [False] * n

def dfs(start):
    stack = [start] # 다시 돌아갈 곳 저장
    visted[start] = True # 시작 정점 방문 처리함

    while stack : # 빈 스택일때까지 반복(다시 돌아갈 곳이 없을때까지)
      cur = stack.pop() # 현재 방문 정점

      for adj in grape[cur]: # 인접한 모든 정점에 대해
        if not visted[adj] : # 아직 방문하지 않았다면
          visted[adj] = True # 방문 처리를 하고
          stack.append(adj) # 스택에 넣는다.
    print(visted)

def[0] # [True, True, True, True, True, True, True]
```