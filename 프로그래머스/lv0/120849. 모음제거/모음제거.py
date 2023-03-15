def solution(my_string):
    m_list = ["a","e","i","u","o"]
    result = ''
    for s in my_string:
        if s not in m_list:
            result += s
    return result