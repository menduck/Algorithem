'''
# 문제 접근
- 다중 집합을 만든다
- Counter를 활용해 집합의 개수를 저장한다.
- set을 통해 교집합과 합집합을 구한다.
- set을 통해 얻은 교집합과 합집합으로 다중집합의 개수를 센다.
  - 교집합은 동일한 집합의 최솟값
  - 합집합은 동일한 집합의 최댓값
- 교집합의 개수/합집합의 개수 * 65536을 정수값만 반환한다.  
  - 교집합이 0일때, 합집합이 0일때의 경우를 따진다.
'''
from collections import Counter

# 두 글자씩 끊어 다중 집합을 만드는 함수(특수문자, 숫자가 들어가면 추가되지 않음)
def make_ele(s):
    str_ele = []
    for i in range(len(s)-1):
        x = s[i:i+2]
        if x.isalpha():
            str_ele.append(x.lower())
    return str_ele

def solution(str1, str2):
    str2_ele = make_ele(str2)
    str1_ele = make_ele(str1)
    str1_ele_count = Counter(str1_ele)
    str2_ele_count = Counter(str2_ele)

    common_ele = list(set(str1_ele) & set(str2_ele))
    total_ele = list(set(str1_ele) | set(str2_ele))

    intersection_count = 0
    for ele in common_ele:
        intersection_count += min(str1_ele_count[ele],str2_ele_count[ele])
    
    union_count = 0
    for ele in total_ele:
        union_count += max(str1_ele_count[ele],str2_ele_count[ele])

    # 집합 모두 공집합일 경우 J(A,B) = 1 임으로 65536으로 반환됨.
    if intersection_count==0 and union_count == 0:
        return 65536
    # 교집합이 0이면 0으로 반환
    elif intersection_count == 0 and union_count > 0:
        return 0
    else:
      return int(intersection_count/union_count * 65536)
            

# print(solution('FRANCE','french'))
# print(solution('aa1+aa2	','AAAA12'))
print(solution('E=M*C^2','e=m*c^2'))