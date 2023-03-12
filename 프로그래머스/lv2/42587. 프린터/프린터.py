'''
# 접근 방법
- 인쇄를 요청한 문서가 정렬되면서 몇 번째 위치하는지 알기위해 딕셔너리 타입으로 저장한다.
    - 인덱스 번호 : 우선 순위 번호
- 우선 순위에 따라 정렬된 리스트를 뽑는다.
- 인쇄를 요청한 문서 인덱스 번호가 정렬된 리스트에 몇 번째 해당되는지 출력한다.
'''
from collections import deque

def solution(priorities, location):
    dict_p = {}
    for i,num in enumerate(priorities):
        dict_p[i] = num
        
    d_priorities = deque(dict_p.items())
    
    # 우선 순위에 따른 출력 순서 
    print_items = []
    while len(print_items) < len(priorities):
        x = d_priorities[0]
        max_num = max(d_priorities, key=lambda x:x[1])
        if x[1] < max_num[1]:
            d_priorities.append(x)
        else:
            print_items.append(x)
        d_priorities.popleft()

    count = 1
    for (i,_) in print_items:
        if i == location:
            return count
        else:
            count += 1


solution([2, 1, 3, 2],2)

# 다른 사람 풀이

# soltuion 2
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            
# solution 3
from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))
    order = 0   # 작업 순서
    while q:
        max_priority = max(q, key=lambda priority: priority[1])   # 작업들 중 가장 높은 중요도
        while q[0][1] < max_priority[1]:
            q.append(q.popleft())
        
        order += 1
        if q[0][0] == location:
            return order
        q.popleft()

    return order

# 내 코드는 우선순위에 따른 출력 순서를 리스트에 담고, 요청한 문서를 찾는 방식이지만,
# 위 두 개 코드 모두 우선 순위에 따라 출력 순서 리스트를 만들면서 요청한 문서가 맨 앞에 놓이면 몇 번째로 출력하는지를 반환한다.
# 요청한 문서가 맨 앞에 올때 뒤 따르는 문서들이 우선 순위에 따르는지 고려할 필요 없기때문에 불필요한 과정을 방지할 수 있다.
'''
# 새롭게 배운 점
- any()
  - 하나라도 True인게 있으면 True
'''