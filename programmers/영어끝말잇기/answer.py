'''
# level2. 영어 끝말 잇기
# 문제 풀이
- words의 첫 단어는 틀릴수가 없으니 검사하지 않는다.
- 검사에 통과한 단어를 배열에 담는다.
  - 두번째 단어부터 첫번째 끝 문자와 같은지 검사한다.
  - 검사에 통과한 단어에 검사할 단어가 중복되지 않는지 검사한다.
- 검사에 통과되지 않으면 [번호, 차례]를 출력한다.
  - 번호는 words의 인덱스를 n으로 나눈 나머지에 +1한 값이다.
    - 만약 n = 3이라면, words의 첫번째 요소의 인덱스는 0
    - (0 % 3) +1 = 1 / 1번 사람이다.
    - words 8번째 요소의 인덱스는 7
    - (7 % 3) +1 = 2 / 2번 사람이다.
  - 차례는 인덱스의 몫에 1을 더한 값이다.
    - 만약 n = 3이라면, words의 두번째 요소의 인덱스는 1
    - (1 // 3) +1 = 1 번째 차례이다.
    - words 8번째 요소의 인덱스는 7
    - (7 // 3) +1 = 3 번째 차례이다.
'''
def solution(n, words):
    valid_words = [words[0]]
    for i in range(1,len(words)): # 두번째 요소부터 끝까지 순회한다.
        if words[i] not in valid_words and valid_words[-1][-1] == words[i][0]:
            valid_words.append(words[i])
        else:
            return [(i%n)+1, (i//n)+1]
            break # 검사에 통과되지 않으면 [번호, 차례]를 출력하고 for문을 종료한다.
    if valid_words == words:
        return [0,0]


# 보완할 점
# - 검사에 통과된 단어들을 valie_words의 배열에 넣지 않고 중복이 되었는지 확인할 수 있다.
# - words[i] in words[:i]
    # - words의 첫 요소부터 i까지 중복된 요소가 있는지 확인한다.
  
def solution(n, words):
    for i in range(1,len(words)): # 두번째 요소부터 끝까지 순회한다.
        if words[i] in words[:i] or words[i-1][-1] != words[i][0]:
            return [(i%n)+1, (i//n)+1]
            break # 검사에 통과되지 않으면 [번호, 차례]를 출력하고 for문을 종료한다.
        else:
          return [0,0]