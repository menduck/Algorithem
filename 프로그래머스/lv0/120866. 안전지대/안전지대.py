'''
# 문제 접근
- 상하좌우대각선 칸에 1이 없는 지역이 몇 개인지 반환하는 문제이다.
- borad의 요소 하나씩 검사한다.
  - 요소의 주위를 모두 검사한다.
  - 범위 내에 존재하고 요소가 1이면 안전지대가 아니므로 0을 반환한다.
  - 모든 검사를 끝낸 요소는 안전지대이므로 1를 반환한다.
'''
# 주위가 모두 0이면 1를 반환하는 함수
def is_safe(x,y,graph):
    # 상하좌우대각선
    dx = [-1,-1,-1,0,0,0,1,1,1]
    dy = [-1,0,1,-1,0,1,-1,0,1]
    n = len(graph)
    
    for k in range(len(dx)):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
            return 0
    return 1
            
            
def solution(board):
    n = len(board)
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                count += is_safe(i,j,board)
    return count
                

    

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))