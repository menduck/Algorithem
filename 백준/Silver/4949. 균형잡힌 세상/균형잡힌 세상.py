import sys

while True:
  s = sys.stdin.readline().rstrip()
  if s == '.':
    break
  unit = {'(':')','[':']'}
  stack = []

  for i in s:
    # i가 문자,공백,온점이면 반복을 건너뛴다.
    if i.isalpha() or i == ' ' or i == '.':
        continue
    # 열린 괄호라면 i를 스택에 추가
    if i in unit.keys():
      stack.append(i)

    # 닫힌 괄호라면
    else:
      if stack: # 빈 스택이 아니면
        if unit[stack[-1]] == i: # 괄호의 짝도 맞으면
          stack.pop() # 스택의 마지막 요소를 제거
        else: # 괄호의 짝이 맞지 않으면 반복문 종료
          stack = True
          break
      else: # 닫힌 괄호고 빈 스택이면 반복문 종료
          stack = True
          break
      
  if stack : # 스택에 값이 있으면 
    print('no')
  else: # 빈 스택이면
    print('yes')