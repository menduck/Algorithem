# - 2번째 줄 input값인 물건의 종류의 수만큼 반복해서 물건의 가격과 개수를 입력받는다.
# - 물건의 가격과 개수를 곱해 모두 더한 다음 1번째 줄의 총 금액과 맞는지 if문으로 확인한다.
# - 맞으면 'Yes', 틀리면 'No'를 출력한다.

import sys
x = int(sys.stdin.readline())
n = int(sys.stdin.readline())

sum = 0
for _ in range(n) :
  price, cnt = map(int, sys.stdin.readline().split())
  sum += (price * cnt) # 가격과 개수를 곱해 sum에 누적합해준다.

if sum == x :
  print("Yes")
else:
  print("No")