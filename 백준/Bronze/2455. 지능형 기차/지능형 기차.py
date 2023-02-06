import sys

# 각 열차에서 타고 있는 사람의 수를 구한다.(탄 사람의 수 - 내린 사람의 수)
result = []
for _ in range(4):
  a,b = map(int, sys.stdin.readline().strip().split())
  if not result: # 빈 배열이면
    result.append(b) # 들어온 사람의 수를 넣는다.
  else:
    result.append(result[-1]+b-a) # 이전 기차에 남아있는 사람의 수와 현재 기차역에서 탄 사람의 수(탄 사람의 수 - 내린 사람의 수)를 더한다.


print(max(result))