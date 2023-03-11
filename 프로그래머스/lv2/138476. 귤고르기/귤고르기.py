'''
# 문제 접근
- 귤 k개를 고를때, 크기가 서로 다른 종류의 최솟값을 구하는 문제
- 종류별 개수를 딕셔너리에 담는다.
  - 종류: 해당 종류의 귤의 개수
- 귤의 개수를 기준으로 내림차순 정렬한다.
- 귤의 개수를 하나씩 순회하면서 누적합해준다.
- k보다 같거나 크면 종류의 개수를 반환한다.
'''

# solution - 성공
from collections import Counter
def solution(k, tangerine):

  # 귤 종류 : 개수 딕셔너리 만든 후 개수를 기준으로 내림차순 정렬
    tangerine_count = sorted(Counter(tangerine).items(),key=lambda x:x[1], reverse=True)
    # tangerine_count = [(3, 2), (2, 2), (5, 2), (1, 1), (4, 1)]

    result= 0
    box = 0

    for (_,count) in tangerine_count:
        box += count
        result += 1
        if box >= k:
            return result


solution(6,[1, 3, 2, 5, 4, 5, 2, 3]	)

# solution - 실패

from collections import Counter
def solution(k, tangerine):

  # 귤 종류 : 개수 딕셔너리 만든 후 개수를 기준으로 내림차순 정렬
    tangerine_count = sorted(Counter(tangerine).items(),key=lambda x:x[1], reverse=True)

    result= 0
    while k > 0:
        for (_,count) in tangerine_count:
            if k >= count:
                k -= count
                result += 1
    return result