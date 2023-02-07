# 1652 누울 자리를 찾아라
'''
# 문제 풀이
- 누울 자리의 조건 
  1. 연속 2칸 이상이고 
  2. 벽이나 짐에 닿아야 한다.

- 가로와 세로의 누울 자리를 구해야 한다.
  - 누울자리를 구하는 함수를 만든다.
  - 행과 열을 바꿔 누울 자리를 구하는 함수에 인자로 넣는다.(세로 누울 자리)

- 행렬의 요소 하나씩 순회한다.
- 한 행 순회 시작
  - 'X'를 만나기 전까지 bed를 하나씩 추가한다.
  - 만약 'X'를 만난다면,
    - bed가 2개 이상이면 카운팅을 세주고
    - bed를 초기화 한다.
- 한 행 순회를 끝나고 bed가 2개 이상이면 카운팅을 해준다.

'''
import sys
n = int(sys.stdin.readline().strip())
matrix = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 행렬의 누울자리(bed라고 지칭함)를 반환하는 함수
def bed_count(matrix,n):
    cnt = 0
    for i in range(n):
        bed = 0
        for j in range(n):
          if matrix[i][j] == '.':
              bed += 1
          else: # 'X' 만났을때
              if bed >= 2: # bed가 2개 이상이면
                  cnt += 1 # 카운트 하나 세주고
              bed = 0 # bed를 초기화 해준다.
        # 만약 한 행의 탐색이 끝나고 bed가 2개 이상이면 카운트를 하나 추가한다.       
        if bed >= 2:
            cnt += 1
    return cnt

# 세로 자리는 열과 행을 바꾸어 함수에 넣어 반환함.
print(bed_count(matrix,n),bed_count(list(zip(*matrix)),n))
행과열이바뀐_matrix = list(zip(*matrix))

'''
print(matrix)
[
  ['.', '.', '.', '.', 'X'],
  ['.', '.', 'X', 'X', '.'],
  ['.', '.', '.', '.', '.'],
  ['.', 'X', 'X', '.', '.'],
  ['X', '.', '.', '.', '.']
]

print(list(zip(*matrix)))
[
  ['.', '.', '.', '.', 'X'],
  ['.', '.', 'X', 'X', '.'],
  ['.', '.', '.', '.', '.'],
  ['.', 'X', 'X', '.', '.'],
  ['X', '.', '.', '.', '.']
]
'''

