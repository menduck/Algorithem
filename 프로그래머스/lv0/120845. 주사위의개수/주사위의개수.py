from functools import reduce
def solution(box, n):
    box_count = list(map(lambda x: x//n,box))
    return reduce(lambda x, y: x*y,box_count)
solution([10, 8, 6],3)