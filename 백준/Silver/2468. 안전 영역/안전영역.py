'''
# 문제 접근
- 안전한 영역의 최댓값을 구한다.

- 물에 잠기는 지점의 범위는 0부터 이차원 배열 요소의  최댓값이다.
- 물에 잠기는 지점에 따라 안전한 영역이 이어지는 개수를 구한다.

'''

# solution - 성공/ dfs

import sys, copy

def dfs(x,y,h):
    # 상하좌우 검사
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]        
    
    # 중복 검사를 막기위해 검사한 요소는 h로 바꿔준다.
    field[x][y] = h

    q = list()
    q.append([x,y])

    # q가 빈배열이면 반복을 중단한다.
    while q:
        # q의 가장 최신 요소를 x,y에 재할당한다.

        x,y = q.pop()
        for i in range(len(dx)):
          nx = x + dx[i]
          ny = y + dy[i]

          # 요소가 범위안에 있고 h보다 크면 안전한 영역이다.
          if 0<=nx<n and 0<=ny<n and field[nx][ny] > h:
              q.append([nx,ny])

              # 중복 검사를 막기위해 검사한 요소는 h로 바꿔준다.
              field[nx][ny] = h
        

n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]


# 이차원 배열의 최댓값을 저장
h = 0
h_max = max(map(max, grid))

safe_area = 0
safe_area_list = []


while h < h_max:
    # 원본 2차원 배열을 깊은 복사한다.
    field = copy.deepcopy(grid)

    for i in range(n):
        for j in range(n):
            if field[i][j] > h:
                safe_area += 1
                dfs(i,j,h)
    safe_area_list.append(safe_area)
    safe_area = 0
    h += 1

print(max(safe_area_list))

'''
# 삽질
- 처음엔 물에 잠기는 지점의 범위가 이차원 배열 요소의 최솟값부터 최댓값이라고 생각했다.
  - ex) 입력값 2 \n 1 1 1 1 일때 기댓값은 1이지만 출력값이 valueError 발생함.
  => 비가 내리는 높이는 0부터 지역의 높이의 최댓값만 고려하면 된다.

- 비가 내리는 높이에 따라 2차원 배열에 원본을 조작하여 안전한 지역이 이어지는 개수를 구했다.
  => 원본이 조작되기때문에 비가 내리는 높이에 따라 원본이 누적되어 훼손된다.
  => 원본을 깊은 복사하여 새로운 변수에 저장하고, 비가 내리는 높이에 따라 원본이 복사된 변수를 사용한다.

# 새롭게 배운점
## 깊은 복사와 얕은 복사
- 객체가 mutable, immutable 경우에 따라 다름
- 얕은 복사
  - list 슬라이싱/ copy모듈를 통해 얕은 복사를 할 경우
  - 새로운 주소값을 받아 원본과 복사본이 서로 영향을 주지 않음
  - 하지만 mutable객체1 안에 mutable객체2일 경우 따로 고려해야함. 
    - mutable객체1은 주소값이 서로 다르지만 mutable객체2의 원본과 복사본의 주소값이 같다.

    ```py
    
    a = [[1,2],[3,4]]

    # slicing
    b = a[:]

    # 주솟값이 다름 => 원본과 복사본이 서로 영향을 주지 않음
    print(id(a) == id(b)) # False

    # mutable객체 안에 mutable한 객체인 경우 같은 주솟값을 가짐 => 원본과 복사본이 서로 영향을 줌
    print(id(a[0]) == id(b[0])) # True

    # 원본이 바뀌면 복사본도 바뀜
    a[0].append("원본 변경")
    print(a) # [[1, 2, '원본 변경'], [3, 4]]
    print(b) # [[1, 2, '원본 변경'], [3, 4]]
    ```

- 깊은 복사
  - 내부에 객체들까지 모두 복사한다.
  - copy.deepcopy()/slicing 를 통해 깊은 복사를 함
  
  ```py
  import copy
  a = [[1,2],[3,4]]
  # deepcopy 사용
  b = copy.deepcopy(a)
  # slicing
  c = [ arr[:] for arr in a]

  a.append([5,6])
  print(a) = [[1,2],[3,4],[5,6]]
  print(b) = [[1,2],[3,4]]
  print(c) = [[1,2],[3,4]]
  ```
'''

