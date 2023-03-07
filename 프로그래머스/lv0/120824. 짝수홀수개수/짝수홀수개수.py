# 문제 접근
# num_list의 짝수의 개수를 먼저 구하고 전체 요소 개수에서 짝수의 개수를 빼 홀수의 개수를 구한다.
# filter를 활용해 짝수만 추출하고 그 개수를 센다.

# solution - filter
def solution(num_list):
    even_count=len(list(filter(lambda x:x%2 == 0, num_list)))
    return [even_count, len(num_list) - even_count]

# 다른 사람 풀이
# soltuion - map
def solution(num_list):
    # 모든 요소를 2로 나눈 나머지로 저장한다.
    div_num_list = list(map(lambda v: v % 2, num_list))
    # 나머지가 0이면 짝수임으로 요소의 0의 개수와 1의 개수를 count로 세서 반환.
    return [div_num_list.count(0), div_num_list.count(1)]