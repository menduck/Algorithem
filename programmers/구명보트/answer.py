'''
# 문제 풀이
- 사람들의 몸무게를 내림차순으로 정렬한다.
- 가장 큰 몸무게부터 순회한다.
- 가장 큰 몸무게와 가장 작은 몸무게의 합이 limit보다 작거나 같으면 두명이 합쳐서 구명보트 1개가 배정된다. => 카운팅 셈
    - 가장 작은 몸무게를 배열에서 제거한다.
- 만약 limit보다 크다면 가장 큰 몸무게인 사람 구명보트 1개 배정 => 카운팅 셈
- 그 다음 큰 몸무게와 배열의 가장 작은 몸무게을 위 과정처럼 계산한다.

'''

def solution(people, limit):
    people_sort =sorted(people, reverse=True) # 80,70,50,50
    cnt = 0
    for p in people_sort: 
        if p + people_sort[-1] <= limit: 
            people_sort.pop()
            cnt += 1
        else:
            cnt += 1

    return cnt

# 코드 리뷰
# - 모든 조건에서 구명보트 개수를 세기 때문에 조건문 밖으로 뺌

def solution(people, limit):
    people_sort =sorted(people, reverse=True) # 80,70,50,50
    cnt = 0
    for p in people_sort: 
        if p + people_sort[-1] <= limit: 
            people_sort.pop() 
        cnt += 1
    return cnt

