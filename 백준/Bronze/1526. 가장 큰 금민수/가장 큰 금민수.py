import sys
N = int(sys.stdin.readline().strip())

while True:
    # 1. 버튼을 True라고 기본값을 설정.
    button = True
    # 2. N을 문자열로 만든 다음 하나씩 순회
    for i in str(N):
        # 3. 4와 7이 없으면  / 3-1. 4 또는 7 중 하나만 있으면 다음 인덱스 순회 / 3-1-1. 모든 인덱스를 순회하여 4와 7 모두 있으면 button은 True상태
        if i != '4' and i != '7':
            # 4. 버튼 False로 끄고 N-1을 해줌 # 3-2. 4 또는 7 중 하나만 있기 때문에 버튼 False 끄고 N-1
            button = False
            N -= 1
    # 5. 버튼이 False이니깐 다시 1번으로 돌아감 / 3-3. 버튼이 False이니깐 다시 1번으로 돌아감 / 3-1-2. 버튼이 True임으로 N을 출력하고 while문을 빠져나간다.
    if button:
        print(N)
        break