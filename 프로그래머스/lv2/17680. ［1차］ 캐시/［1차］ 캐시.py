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