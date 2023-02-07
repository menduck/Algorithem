# 1063 킹

'''
# 문제풀이
- 킹이 움직일 수 있는 키워드를 딕셔너리로 방향을 저장한다.
- 킹의 위치와 돌의 위치를 인덱스 번호로 바꾼다.
- 조건에 성립하면 위치를 이동한다.
    - 체스 범위 안에 위치해야하고
    - 킹의 이동할 위치가 돌의 위치면 돌은 킹의 방향만큼 이동한다.
        - 단, 돌이 체스 범위 안에 위치할때만
- 조건이 성립하면 인덱스 번호를 다시 체스판에 맞게 출력한다.
'''
# soltuion1 - 시도/성공

# delta = {
#     'R':(1,0),
#     'L':(-1,0),
#     'B':(0,1),
#     'T':(0,-1),
#     'RT':(1,-1),
#     'LT':(-1,-1),
#     'RB':(1,1),
#     'LB':(-1,1)
# }
# # 입력값을 행렬 인덱스로 바꿔주는 함수
# def change_matrix_point(point):
#     col = 'ABCDEFGH'
#     x = col.index(point[0])
#     y = 8 - int(point[1])
#     return x,y

# matrix = [[0]*8 for _ in range(8)]

# import sys
# king,stone,n = sys.stdin.readline().strip().split()

# k_x,k_y = change_matrix_point(king)
# s_x,s_y = change_matrix_point(stone)


# move_data = [sys.stdin.readline().strip() for _ in range(int(n))]
# move_point = [delta[m] for m in move_data]


# for m in range(int(n)):
#     # 킹의 위치는 범위에 벗어나지 않으면 움직인다.
#     if 0 <= k_x +  move_point[m][0] < 8 and 0<= k_y +  move_point[m][1] < 8:
#         k_x += move_point[m][0]
#         k_y += move_point[m][1]
#     # 만약 움직인 킹의 위치와 돌의 위치가 같으면
#     if k_x == s_x and k_y== s_y :
#         # 돌의 위치가 킹의 위치때문에 움직인 위치가 범위에 벗어나지 않으면 움직이고
#         if 0 <= s_x +  move_point[m][0] < 8 and 0<= s_y +  move_point[m][1] < 8:
#             s_x += move_point[m][0]
#             s_y += move_point[m][1]
#         # 돌의 위치가 킹의 위치때문에 움직인 위치가 범위에 벗어나면 돌은 움직이지 않고 킹도 원래 위치로 돌아간다.
#         else:
#             k_x -= move_point[m][0]
#             k_y -= move_point[m][1]


# # 함수 인덱스를 체스판 숫자로 바꿔주는 함수
# def change_chess_point(x,y):
#     col = 'ABCDEFGH'
#     c_x = col[x]
#     c_y = str(8 - y)
#     return c_x + c_y

# print(change_chess_point(k_x,k_y))
# print(change_chess_point(s_x,s_y))

'''
# 보완할 점.
- 알파벳을 아스키 코드로 변환하여 쓴다.
    - 현재 : 'A1'을 입력받으면 'ABCDEFGH'에서 'A'의 인덱스 번호를 구해 열의 값을 구하고 '1'은 8에서 빼 0에서 부터 시작하는 행의 값을 구한다.
    - 보완 : 아스키코드를 이용해 알파벳을 쉽게 인덱스 번호로 바꾸고 행은 그냥 입력받는다.(행의 시작을 1로) => delta값 다시 설정해야 한다.
- if조건문을 간단히 만들자.
    - 현재 : 이동한 다음 체스판에 벗어나면 다시 이동 전의 위치로 이동한다.
    - 보완 : 이동값을 저장하고 체스판에 벗어나지 않으면 현재 위치에 이동값을 더해 이동한다.

'''

# solution - 최종 코드/성공
delta = {
    'R':(1,0),
    'L':(-1,0),
    'B':(0,-1),
    'T':(0,1),
    'RT':(1,1),
    'LT':(-1,1),
    'RB':(1,-1),
    'LB':(-1,-1)
}

import sys
king,stone,n = sys.stdin.readline().strip().split()

# 킹의 위치와 돌의 위치를 인덱스 번호로 바꿈
k_x,k_y = ord(king[0]) -64, int(king[1])
s_x,s_y  = ord(stone[0]) -64, int(stone[1])

move_data = [sys.stdin.readline().strip() for _ in range(int(n))]
move_point = [delta[m] for m in move_data]


for m in range(int(n)):
    # 킹은 입력받은 움직이는 값만큼 이동값을 가진다.(아직 움직이는거 아님) 
    move_k_x = k_x + move_point[m][0]
    move_k_y = k_y + move_point[m][1]
    # 킹의 위치가 체스 밖에 벗어나지 않고
    if 0 < move_k_x <= 8 and 0 < move_k_y <= 8:
        # 킹의 위치와 돌의 위치가 같고
        if move_k_x == s_x and move_k_y == s_y:
            # 돌의 위치는 킹이 움직이는 만큼 이동값을 가진다. (아직 킹의 위치도 같이 이동하는 것이 아님)
            move_s_x = s_x + move_point[m][0]
            move_s_y = s_y + move_point[m][1]
            # 만약 돌의 위치가 체스 밖에 벗어나지 않으면
            if 0 < move_s_x <= 8 and 0 < move_s_y <= 8:
                # 킹과 돌은 각자의 이동값만큼 움직인다.
                k_x, k_y = move_k_x, move_k_y
                s_x, s_y = move_s_x, move_s_y
        # 만약 킹이 이동할때 돌의 위치가 상관없으면 킹은 이동값만큼 움직인다.
        else:
            k_x, k_y = move_k_x, move_k_y
            

print(chr(k_x + 64), k_y, sep ='')
print(chr(s_x + 64), s_y, sep ='')