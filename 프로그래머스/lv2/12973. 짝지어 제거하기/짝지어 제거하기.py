def solution(S):
  stack = []
  for word in S:
    if not stack: # 빈 배열이면
      stack.append(word)
    elif stack[-1] == word:
      stack.pop()
    else:
      stack.append(word)
  if not stack:
    return 1
  else:
    return 0
