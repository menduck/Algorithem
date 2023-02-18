# 위장

'''
# 문제풀이
- 종류별로 몇 개가 있는지 딕셔너리 저장
  - key는 종류 value는 종류의 옷 개수

- 만약 {티셔츠:2,신발:3,모자:1} 일 경우 경우의 수는
2+3+1+(2*3)+(2*1)+(3*1)+(2*3*1)이다.
- combination으로 중복되지 않는 조합을 list로 저장하고 각 요소들을 곱해 누적합을 구한다.

https://velog.io/@so-soon/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%EC%9E%A5
https://school.programmers.co.kr/questions/25816
'''

# soltuion - 1번 케이스 초과
from itertools import combinations
from math import prod

def solution(clothes):
    clothes_count = {}
    for set in clothes:
        if set[1] in clothes_count:
            clothes_count[set[1]] += 1
        else:
            clothes_count[set[1]] = 1
    # print(clothes_count) {'headgear': 2, 'eyewear': 1}
    
    items_count = clothes_count.values()
    # items_count = (3,)
    result = sum(items_count)

    if len(items_count) == 1:
      return result

    for i in range(2, len(items_count)+1):
        combi = list(map(list,combinations(items_count,i)))
        result += sum(map(lambda x: prod(x) ,combi))
        # print(combi) 
        # [[2, 3], [2, 1], [3, 1]]
        # [[2, 3, 1]]
    return result


