def solution(brown, yellow):
    for i in range(1, yellow+1):
        if 2*i +2*yellow/i +4 == brown:
            if i >= yellow//i :
                return [i+2,yellow//i +2]