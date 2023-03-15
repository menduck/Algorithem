def solution(dots):
    dots_sort = sorted(dots, key=lambda x: sum(x))
    min_p, max_p = dots_sort[0], dots_sort[-1]
    return (max_p[0]-min_p[0]) * (max_p[1]-min_p[1])


solution([[1, 1], [2, 1], [2, 2], [1, 2]])

# 다른 사람 풀이
# solution
def solution(dots):
    return (max(dots)[0] - min(dots)[0])*(max(dots)[1] - min(dots)[1])

# sort 하지 않아도 max,min을 활용하면 가장 작은 좌표와 큰 좌표를 구할 수 있다.
# 리스트 안에 리스트에 첫번째 요소를 비교하고 같으면 두 번째 요소를 비교해 가장 큰 값 또는 작은 값을 반환한다.