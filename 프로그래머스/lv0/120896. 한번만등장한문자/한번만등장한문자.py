'''
# 문제 접근
- Counter 이용하여 문자 중복 개수를 세줌
- filter로 문자 중복 개수가 1인 튜플만 추출하고 문자를 오름차순으로 정렬
- 튜플의 첫 번째 요소만 순회하면서 저장하고 반환한다.
'''
from collections import Counter

def solution(s):
    s_only_one = list(filter(lambda x: x[1] == 1, Counter(s).items()))
    sorted_s = sorted(s_only_one,key=lambda x:x[0])
    
    result = ''
    for s in sorted_s:
        result += s[0]
    return result