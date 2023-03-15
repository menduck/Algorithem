def solution(rsp):
    rsp_list = list(rsp)
    result = ''
    for r in rsp_list:
        if r == '2':
            result += '0'
        if r == '0':
            result += '5'
        if r == '5':
            result += '2'
    return result