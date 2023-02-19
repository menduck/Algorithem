'''
# 문제풀이
- 길이로 오름차순 정렬
- 하나씩 차집합 이어 붙이기
'''

# solution1 - 차집합 활용
def solution(s):
    # 입력값 전처리
    s = s[2:-2] # 젤 앞뒤 괄호 삭제
    s_not_bracket = s.replace('{','').replace('}',' ')
    s_list = s_not_bracket.split(' ,')
    s_int = list(map(lambda x : list(map(int,x.split(','))),s_list))


    s_int.sort(key = len)

    answer = s_int[0]

    for i in range(1,len(s_int)):
        temp = set(s_int[i]) - set(answer)
        answer.append(*temp)

    return answer
        
        
# solution2 - not in 활용
def solution(s):
    # 입력값 전처리
    s = s[2:-2] # 젤 앞뒤 괄호 삭제
    s_not_bracket = s.replace('{','').replace('}',' ')
    s_list = s_not_bracket.split(' ,')
    s_int = list(map(lambda x : list(map(int,x.split(','))),s_list))


    s_int.sort(key = len)

    answer = []
    for ele_s in s_int:
        for ele in ele_s:
            if ele not in answer:
                answer.append(ele)
    return answer
