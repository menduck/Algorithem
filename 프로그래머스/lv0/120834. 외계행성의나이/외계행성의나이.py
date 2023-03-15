def solution(age):
    alphabet = list('abcdefghijklnmopqrstuvwxyz')
    
    result = ''
    for num in list(str(age)):
        result += alphabet[int(num)]
    return result

