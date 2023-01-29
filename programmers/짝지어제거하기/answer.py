'''
# 문제 풀이
- 문자열 중 짝지어진 문자를 제거한 뒤, 이어 붙여 짝지어지 문자를 모두 제거한다.
- 남겨진 문자가 없으면 1를 있으면 0을 반환한다.

- 스택을 사용하여 풀었다.

# solution - 실패

```py
def solution(S):
  stack = []
  for word in S:
    if not stack: 
      stack.append(word)
    elif stack[-1] == word:
      stack.pop()
  if not stack:
    return 1
  else:
    return 0

print(solution(S))
```

# 반례
- S = 'abcda'일때 기대값은 0이지만 출력값은 1이 나옴.
- 짝지어진 단어가 아닐때 실행하는 코드가 없기때문에
- S의 첫번째 요소인 a가 들어가면 d가 들어올때까지 stack엔 a만 남고 마지막 요소인 a가 들어오면 pop되어 stack이 빈 배열이되므로 1를 리턴한다.

# solution - 성공
def solution(S):
  stack = []
  for word in S:
    if not stack: # 빈 배열이면
      stack.append(word) # stack에 문자를 추가하고
    elif stack[-1] == word: # stack에 가장 최신 데이터가 문자와 같다면 제거한다.
      stack.pop()
    else: # 짝지어진 문자가 아니라면
      stack.append(word) # stack에 추가한다
  if not stack:
    return 1
  else:
    return 0
'''
# 코드리뷰
# 문자열의 길이가 홀수면 바로 0을 리턴한다.

def solution(S):

  if len(S)%2:
    return 0
  
  stack = []
  for word in S:
    if not stack: # 빈 배열이면
      stack.append(word) # stack에 문자를 추가하고
    elif stack[-1] == word: # stack에 가장 최신 데이터가 문자와 같다면 제거한다.
      stack.pop()
    else: # 짝지어진 문자가 아니라면
      stack.append(word) # stack에 추가한다
  if not stack:
    return 1
  else:
    return 0