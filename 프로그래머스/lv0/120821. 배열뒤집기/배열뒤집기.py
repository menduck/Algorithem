# 문제 접근
# 배열 뒤집기

# 슬라이싱을 활용하여 뒤집기
def solution(num_list):
    return num_list[::-1]

# reversed를 활용하여 뒤집기
def solution(num_list):
    return list(reversed(num_list))
# reversed는 객체를 반환하기 때문에 list로 변환해야 한다.

# for문으로 뒤집기
def solution(num_list):
    result = []
    for i in range(1,len(num_list)+1):
        # num_list 젤 뒷 요소부터 접근하여 result에 추가함.
        result.append(num_list[-i])
    return result