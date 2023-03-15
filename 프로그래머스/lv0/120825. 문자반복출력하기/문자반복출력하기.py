def solution(my_string, n):
    result = ''
    for s in my_string:
        result += s*n
    return result

# 다른 사람 풀이
def solution(my_string, n):
    return ''.join(i*n for i in my_string)