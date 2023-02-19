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