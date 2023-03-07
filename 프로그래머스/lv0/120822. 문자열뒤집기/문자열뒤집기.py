# 문제 접근
# 문자열 뒤집기

# solution - 슬라이싱
def solution(my_string):
    return my_string[::-1]

# solution - reversed
def solution(my_string):
    # list를 str으로 타입을 바꾸기 위해 join을 활용함.
    return ''.join(list(reversed(my_string)))

# soltuion - for
def solution(my_string):
    result_str = ""
    for char in my_string:
        result_str = char + result_str
    return result_str