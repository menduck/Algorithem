# 17608 막대기

# solution1 - 시간 초과
import sys
n = int(sys.stdin.readline().strip())
bar_numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

cnt = 0
for i in range(n-1):
    # 현재값이 나머지값들의 최댓값보다 크면 보는 방향에서 보이기때문에 카운팅 해줌
    if bar_numbers[i] > max(bar_numbers[i+1::]):
        cnt +=1
print(cnt+1)

# bar_number를 순회(O(n))하면서 max값(O(n)을 찾아 비교하기 때문에 위 연산의 시간복잡도는 O(n^2)이다.

# soltuion2 - 성공
import sys
n = int(sys.stdin.readline().strip())
bar_numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

cnt = 0
# 최솟값을 보는 방향에서 젤 앞에 있는 막대로 설정
min = bar_numbers[-1]

# 보는 방향에서 두번째 막대부터 순회함
for i in range(n-2,-1,-1):
    # 만약 최솟값보다 막대 번호가 크다면 그 번호로 최솟값으로 바꾸고 카운트해줌
    if bar_numbers[i] > min:
          min = bar_numbers[i]
          cnt +=1
print(cnt+1)