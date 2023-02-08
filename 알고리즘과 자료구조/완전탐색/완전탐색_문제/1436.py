# 1436 영화 감독 숌
'''
# 문제 풀이
- '666'이 포함되는 숫자를  666부터 1씩 증가하면서 완전탐색한다.
'''
# soltuion - 최종코드
import sys
n = int(sys.stdin.readline().strip())

target_number = 666

while n:
    if '666' in str(target_number):
        n -= 1
    target_number += 1
print(target_number-1)


# solution - 실패
'''
## 문제 풀이
- 666 앞에 1씩 증가하는 수를 붙인다.
- 666 뒤에 1씩 증가하는 수를 붙인다.
- 두 수를 비교하여 더 작은 값이 result로 값을 갱신한다.

## 실패 이유
- n = 26일때 15666
- n = 27일때 16660이 나와야되는데 출력값이 17666으로 나옴
- f_count가 16일될때 일의 자리 6도 연속된 6문자에 포함되지 않음.
'''
import sys
n = int(sys.stdin.readline().strip())
count = 0
f_count = 0
b_count = 0
while True:
    result = 666
    if '666' in str(result):
      f_six = int(str(f_count)+str(result))
      b_six = int(str(result)+str(b_count))
      if f_six >= b_six:
          result = b_six
          b_count += 1
      else:
          result = f_six
          f_count += 1

    if n-1 == count:
        print(result)
        break
    count += 1