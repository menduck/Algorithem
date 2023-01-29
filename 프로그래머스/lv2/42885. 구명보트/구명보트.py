def solution(people, limit):
    people_sort =sorted(people, reverse=True) # 80,70,50,50
    cnt = 0
    for p in people_sort:
        cnt += 1
        if p + people_sort[-1] <= limit: 
            people_sort.pop() 
        
    return cnt
