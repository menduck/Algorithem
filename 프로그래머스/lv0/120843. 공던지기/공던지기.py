def solution(numbers, k):
    circle_number = numbers*k
    ball_number = circle_number[::2]
    return ball_number[k-1]
solution([1, 2, 3, 4],2)