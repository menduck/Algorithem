'''
# 문제풀이
- 길이로 오름차순 정렬
- 하나씩 차집합 이어 붙이기
'''

def solution(s):
    # 입력값 전처리
    s = s[2:-2] # 젤 앞뒤 괄호 삭제
    s_not_bracket = s.replace('{','').replace('}',' ')
    s_list = s_not_bracket.split(' ,')
    s_int = list(map(lambda x : list(map(int,x.split(','))),s_list))
  

    s_int.sort(key = len)

    answer = s_int[0]
    temp_set = set(s_int[0])

    for i in range(1,len(s_int)):
        temp = set(s_int[i]) - temp_set
        answer.append(*temp)
        temp_set.add(*temp)

    return answer
        
        

    


solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
