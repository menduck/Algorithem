# solution - 실패
def solution(citations):
    citations.sort(reverse = True)
    if set(citations) == {0}:
        return 0
    if len(set(citations)) == 1:
        return len(citations)
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i

# 입력값 [100,50,10] 기대값 3 출력값 null

# solution2 - 성공
def solution(citations):
    citations.sort(reverse = True)
    if citations[0] == 0:
        return 0
    if len(set(citations)) == 1:
        return len(citations)
    
    for i in range(len(citations)):
        if i+1 > citations[i]:
            return i
    return i+1


# enumerate 이용해보기
def solution(citations):
    citations.sort(reverse=True)
    return max(map(min, enumerate(citations, start=1)))