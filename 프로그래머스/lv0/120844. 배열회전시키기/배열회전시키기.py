from collections import deque

def solution(numbers, direction):
    d = {'right':1, 'left':-1}
    deque_numbers = deque(numbers)
    deque_numbers.rotate(d[direction])
    return list(deque_numbers)