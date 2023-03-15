'''
# 문제접근
- 문자 하나씩 순회하면서 숫자이면 임시변수에 저장하고 숫자가 아닌 문자를 만났을때 임시변수에 저장해 놓은 문자열을 리스트에 추가한다.
- 리스트에 있는 요소를 정수형으로 바꿔준 후 모두 더해 반환한다.
'''

def solution(my_string):
    num_list = []
    tmp = ""
    for char in my_string:
        if char.isdigit():
            tmp += char
        else:
            if tmp:
              num_list.append(tmp)
              tmp = ""
    num_list.append(tmp) if tmp else 0
    
    return sum(map(int,num_list))

solution("aAb1B2cC34oOp")

# 다른 사람 풀이

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())
