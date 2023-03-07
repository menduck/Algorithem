# 문제 접근
# 슬라이싱을 활용하여 원하는 인덱스 범위만 반환한다.
# list[시작 인덱스, 끝 인덱스]
# 주의할 점은 끝 인덱스는 포함되지 않는다라는 것이다. 문제에선 num2까지 포함하여 반환하기 때문에 +1을 해주었다.

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]