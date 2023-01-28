# 카펫

def solution(brown, yellow):
  for x in range(1, yellow+1):
    if 2*x +2*yellow/x +4 == brown:
      if x >= yellow//x :
        return [x+2,yellow//x +2]

'''
# 문제 풀이
- yellow의 가로를 x, 세로를 yello/x

- brown = 2x + 2(yello/x) + 4
- yellow = x(yello/x) = yello
- [가로,세로] = [x+2, yello/x +2]

- for문으로 1부터 yellow 수까지 순회하면서 조건에 맞는 가로 x 값을 찾고 가로와 세로를 반환한다.
'''