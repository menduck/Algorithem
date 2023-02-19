# 위장

'''
# 문제풀이
- 종류별로 몇 개가 있는지 딕셔너리 저장
  - key는 종류 value는 종류의 옷 개수

- 만약 {티셔츠:2,신발:3,모자:1} 일 경우 경우의 수는
2+3+1+(2*3)+(2*1)+(3*1)+(2*3*1)이다.
- combination으로 중복되지 않는 조합을 list로 저장하고 각 요소들을 곱해 누적합을 구한다.

'''

# soltuion1 - 실페/1번 케이스 시간 초과
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

'''
# 보완할 점
- 모든 조합을 찾아서 해결하는 과정의 시간 복잡도가 매우 높기 때문에 시간을 줄여야 한다.

- 종류별로 몇 개가 있는지 딕셔너리 저장
  - key는 종류 value는 종류의 옷 개수

- 만약 {티셔츠:2,신발:3,모자:1} 일 경우 
- (티셔츠 2가지 + 티셔츠 안입는 경우) *  (신발 3가지 + 신발 안신는 경우) * (모자 1가지 + 모자 안쓰는 경우) - (맨 몸인 경우)
- (2+1)*(3+1)*(1+1) - 1

'''

# soltuion2 - 최종코드 / 성공
def solution(clothes):
    clothes_count = {}
    for _,category in clothes:
        if category in clothes_count:
            clothes_count[category] += 1
        else:
            clothes_count[category] = 1
    # print(clothes_count) {'headgear': 2, 'eyewear': 1}
    
    result = 1
    for key in clothes_count:
      result *= clothes_count[key] +1
    return result -1

# solution3 - solution2와 같은 알고리즘이지만 내장 모듈을 잘 썼음.
def solution(clothes):
    from collections import Counter
    from functools import reduce
    # 종류별로 몇 개가 있는지 Counter를 활용하여 세줌
    cnt = Counter([kind for _, kind in clothes])
    # x는 누적값, y는 현재값
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

# print(solution2([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))