# 문제 접근
# 각각 조건식을 작성하여 해당되면 리턴값을 반환함.

def solution(angle):
    if 0 < angle < 90:
        return 1
    if angle == 90:
        return 2
    if 90 < angle < 180:
        return 3
    if angle == 180:
        return 4

# 다른 사람 풀이
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    # (angle % 90 > 0)이 true이면 1를 false이면 0으로 계산됨.
    return answer