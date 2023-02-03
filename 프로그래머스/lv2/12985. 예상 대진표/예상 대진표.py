def exponent_two(number):
    cnt = 0
    while number >1:
        number = number/2
        cnt += 1
    return cnt

def solution(n,a,b):
    while n > 1: # 4
        half_stage = n/2 + 0.5
        if (a < half_stage and half_stage< b) or (b < half_stage and half_stage< a) :
            return exponent_two(n) #1
        else:
            a =  a - n/2 if a - n/2 > 0 else a
            b =  b - n/2 if b - n/2 > 0 else b
            n = n/2