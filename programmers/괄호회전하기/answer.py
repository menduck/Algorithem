# 괄호 회전하기
'''
# 문제 풀이
- 문자열을 최대 문자열 길이까지 순차적으로 회전시켰을 때, 올바른 괄호 문자열이 되게 하는 x의 개수를 구하는 문제
'''
from collections import deque

# 올바른 문자열인지 확인하는 함수(올바른 문자열이면 1를 올바르지 않다면 0을 반환함)
def is_bracket_str(target_str):
    bracket = {'(':')','{':'}','[':']'}
    stack = []

    for s in target_str:
        # 열린 괄호라면
        if s in bracket.keys():
            # 스택에 추가함
            stack.append(s)
        
        # 닫힌 괄호라면
        else:
          # 빈 스택이 아니라면
            if stack:
                # 스택에 넣은 최신 요소의 짝과 검사하고 있는 괄호가 같다면
                if bracket[stack[-1]] == s:
                    # 스택에 최신 요소를 제거한다.
                    stack.pop()
                # 스택에 넣은 최신 요소의 짝과 검사하고 있는 괄호가 같지 않다면
                else:
                    # 반복을 중단한다.
                    stack = True
                    break
            # 빈 스택이면  
            else:
                # 반복을 중단한다.
                stack = True
                break

    # 빈 스택이면 올바른 괄호 문자열    
    if not stack:
        return 1
    else:
        return 0

def solution(s):
    count = 0
    target = deque(s)
    max_rotate = len(target)
    # deque의 rotate을 활용해서 왼쪽으로 한칸씩 회전하면서 올바른 문자열인지 확인하고 카운트 한다.
    while max_rotate > 0:
        target.rotate(-1)
        count += is_bracket_str(target)
        max_rotate -= 1
    return count

