def gcd(a, b):  
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    new_lcm = lcm(denom1,denom2)
    new_numer = numer1*(new_lcm//denom1) + numer2*((new_lcm//denom2))
    new_gcd = gcd(new_lcm,new_numer)
    return [new_numer/new_gcd, new_lcm/new_gcd]