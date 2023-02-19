def solution(clothes):
    clothes_count = {}
    for _,category in clothes:
        if category in clothes_count:
            clothes_count[category] += 1
        else:
            clothes_count[category] = 1
    # print(clothes_count) {'headgear': 2, 'eyewear': 1}
    
    result = 1
    for key in clothes_count:
        result *= clothes_count[key] +1
    return result -1