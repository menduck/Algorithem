'''
# 문제 접근
- 아래의 조건을 만족하는 나머지 한 변이 될 수 있는 정수의 개수
  - 가장 긴 변의 길이 < 다른 변의 길이 + 또 다른 변의 길이

- 가장 긴 변의 길이를 찾아야 한다.
  - 배열 sides 중 하나가 가장 긴 변의 길이일 경우
    - 배열 sides 요소 사이의 개수 정수부터 가장 긴 변의 길이까지 나머지 한 변이 될 수 있다.
  -  나머지 한 변이 가장 긴 변의 길이일 경우
    
'''
def solution(sides):
    sides.sort()
    max_len = sides[1]
    return len(range(max_len - sides[0] +1,max_len+1)) + len(range(max_len+1,sum(sides)))

# 다른 사람 풀이

# solution - 수학적 풀이
def solution(sides):
    return 2 * min(sides) - 1

'''
- 기존 변 a,b(a>b)
- 나머지 한 변이 c라고 할때 경우의 수는 3가지이다.
- 1) a>b, a>c 일 경우(배열 sides 중 하나가 가장 긴 변의 길이일 경우)
  - b+c > a 이므로 b+c>a>c 이다.
  - b>a>0이 되므로 a의 개수는 b-1 개이다.
- 2) c>a>b 일 경우(나머지 한 변이 가장 긴 변의 길이일 경우)
  - a+b>c 이므로 a+b>c>a이다.
  - b>c>0 이므로 c의 개수는 b-1개 이다.
- 3) c == a 일 경우는 1번이다.

- 총 개수는 b-1 + b-1 +1 = 2b - 1 개이다.
- 여기서 b는 sides 배열의 최솟값이다.
'''