def solution(numbers):
    positive_num = []
    negative_num = []
    for num in numbers:
        if num< 0:
            negative_num.append(num)
        else:
            positive_num.append(num)
    positive_num.sort()
    negative_num.sort()
    
    if len(positive_num) > 1:
        if len(negative_num) > 1:
            return max(positive_num[-1]*positive_num[-2], negative_num[-1]*negative_num[-2])
        else:
            return positive_num[-1]*positive_num[-2]
    else:
        if len(negative_num) > 1 :
            return negative_num[-1]*negative_num[-2]
        else:
            return numbers[0] * numbers[1]

        
print(solution([-1,2]))

# 다른 사람 풀이
# solution
def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])

# 굳이 음수와 양수 리스트를 나눠 경우를 따지지 않아도 된다.
