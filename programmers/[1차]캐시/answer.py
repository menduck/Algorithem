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

# solution - 성공
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


# solution2 - 성공/if문 정리하기
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

        # 동일한 값이 있으면(cache hits) 1를 누적해주고 동일한 값을 제거한다.
        if city in stack:
            time += 1
            stack.remove(city)
            
        # 동일한 값이 없고(cache miss) cache size보다 크면 오래된 데이터는 제거한다.
        else:
            time += 5
            if len(stack) >= cacheSize :
                    stack.popleft()
        
        # 새로운 도시를 스택에 추가한다.
        stack.append(city)
    return time

#  - if문 중복된 코드 제거하기
#   - 조건마다 마지막에 새로운 도시를 스택에 추가해줘야 되기때문에 조건문 밖에서 마지막에 추가를 해준다.

# solution - 성공/maxlen 

from collections import deque
def solution(cacheSize, cities):
    stack = deque([],cacheSize) 
    time = 0

    # 만약 캐시크기가 0이면 모든 요소들이 cache miss이다.
    if cacheSize == 0:
      return len(cities) * 5
    
    for city in cities:
        # 대소문자 관계 없으므로 모든 요소 소문자로 변환
        city = city.lower()

        # 동일한 값이 있으면(cache hit) 1를 누적해주고 동일한 값을 제거한다.
        if city in stack:
            time += 1
            stack.remove(city)
            
        # 동일한 값이 없으면(cache miss) 5를 누적해 준다.
        else:
            time += 5
        
        # 새로운 도시를 스택에 추가한다.
        stack.append(city)
    return time
'''
## maxlen
> deque(iterable,maxlen)

- deque 길이의 최댓값을 설정할 수 있다.
- deque에  maxlen 이상의 값을 추가할 경우, maxlen 길이의 맞게 값이 삭제된다.
    - append()로 값을 추가할 경우, 가장 오래된 데이터(맨 왼쪽 요소)가 삭제된다.
    - appendleft()로 값이 추가할 경우, 가장 최신 데이터(맨 오른쪽 요소)가 삭제된다.

'''