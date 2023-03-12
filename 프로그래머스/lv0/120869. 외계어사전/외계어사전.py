# solution - 실패

def solution(spell, dic):
    for word in dic:
        if all(w in spell for w in word):
            return 1
        else:
            continue
    return 2
'''
# 실패 이유            
- spell의 원소 모두 사용해 단어를 만들어야 하는 조건 불충족
- all(w in spell for w in word)에서 spell 요소 중 한가지로만 이룬 word도 True이다.
'''

# solution - 성공
'''
# 문제 접근
- spell의 요소를 하나씩 순회한다.
    - filter로 그 요소가 포함되어 있는 단어를 추출한다.
    - 추출한 리스트에 그 다음 spell의 요소가 포함되어 있는지 추출한다.
    - spell의 모든 요소를 순회할때까지 반복한다.
- 만약 추출된 리스트가 있다면 1를 반환하고 없다면 2를 반환한다.

# 시간 복잡도
- 첫 번째 for문은 spell의 크기에 비례하므로 시간복잡도는 O(n)이다.
- filter 의 시간 복잡도도 result 크기에 비례하므로 시간 복잡도는 O(n)이다.
- 전체 시간 복잡도는 O(len(spell)*len(dic)), 즉 O(n^2) 이다.
'''

def solution(spell, dic):
    result = dic
    for ele in spell: 
        words = list(filter(lambda x: ele in x, result))
        if words :
            result = words
        else:
            break

    if words:
        return 1
    else:
        return 2
        


print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
