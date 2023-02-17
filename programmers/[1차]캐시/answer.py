# [1차]캐시
'''
# LRU 알고리즘
- 페이지 부재가 발생했을 경우 가장 오랫동안 사용되는 페이지를 제거하는 알고리즘

- 캐시 크기가 정해져 있고 캐시 크기 만큼 페이지를 받고 그 이상의 페이지를 받을때
- 만약 동일한 값이 있다면 가장 최신 값으로 변경
- 동일한 값이 없다면 가장 오래된 값을 제거하고 새로운 값을 넣는다.

# 문제 풀이
- 빈 스택을 만들어 도시를 하나씩 넣는다.
- 스택의 크기는 최대 캐시 크기이다.
- 만약 스택에 동일한 도시가 있다면 가장 최신 값으로 변경한다. 이 경우 cache hit임으로 실행시간 1를 누적한다.
- 만약 동일한 도시가 없다면 스택에 가장 오래된 값을 제거하고 새롭게 값을 추가 한다. 이경우 cache miss임으로 실행시간 5를 누적한다.

=================================================
예제

cacheSize = 2 
dities = ["Jeju", "Pangyo", "NewYork", "newyork"]

['jeju'] 실행 시간 :  5
['Jeju', 'Pangyo'] 실행 시간 : 5
['Pangyo','NewYork'] 실행 시간 : 5
['Pangyo','newYork'] 실행 시간 : 1

총 실행 시간 : 16
'''
from collections import deque
def solution(cacheSize, cities):
    stack = deque()
    time = 0

    # 만약 캐시크기가 0이면 모든 요소들이 cache miss이다.
    if cacheSize == 0:
      return len(cities) * 5
    
    for city in cities:
        # 대소문자 관계 없으므로 모든 요소 소문자로 변환
        city = city.lower()

        # 동일한 값이 있으면 동일한 값 삭제하고 최신 값으로 추가한다.
        if city in stack:
            time += 1
            stack.remove(city)
            stack.append(city)

        # 동일한 값이 없으면 
        else:
            time += 5
            # cache size보다 배열의 크기가 작으면
            if len(stack) < cacheSize:
                # 값을 추가
                stack.append(city)
            # cache size보다 배열의 크기가 크면 가장 오래된 데이터 삭제하고 최신 값 추가
            else:
                stack.popleft()
                stack.append(city)
    return time

