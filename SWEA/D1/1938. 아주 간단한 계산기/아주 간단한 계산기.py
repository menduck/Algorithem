# 문제 풀이
# - 두 자연수를 공백으로 구분하여 입력받는다.
# - 두 자연수를 +,-,*,/ 계산한 값(소수점 이하는 버림)를 한줄에 한개씩 출력한다.

# 코드
import math
a, b = map(int, input().split())
print(math.floor(a+b)) 
print(math.floor(a-b)) 
print(math.floor(a*b)) 
print(math.floor(a/b)) 