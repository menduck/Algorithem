# 문제 접근
# 배열의 요소마다 길이를 리스트로 반환한다.
# map을 사용하여 요소에 접근하고 길이를 반환한다.

# solution - 성공
def solution(strlist):
    return  list(map(lambda x : len(x), strlist))
