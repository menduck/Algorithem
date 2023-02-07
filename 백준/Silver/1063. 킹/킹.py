# 1063 킹

delta = {
    'R':(1,0),
    'L':(-1,0),
    'B':(0,1),
    'T':(0,-1),
    'RT':(1,-1),
    'LT':(-1,-1),
    'RB':(1,1),
    'LB':(-1,1)
}
def change_matrix_point(point):
    col = 'ABCDEFGH'
    x = col.index(point[0])
    y = 8 - int(point[1])
    return x,y

matrix = [[0]*8 for _ in range(8)]

import sys
king,stone,n = sys.stdin.readline().strip().split()

k_x,k_y = change_matrix_point(king)
s_x,s_y = change_matrix_point(stone)


move_data = [sys.stdin.readline().strip() for _ in range(int(n))]
move_point = [delta[m] for m in move_data]


for m in range(int(n)):
    if 0 <= k_x +  move_point[m][0] < 8 and 0<= k_y +  move_point[m][1] < 8:
        k_x += move_point[m][0]
        k_y += move_point[m][1]
    if k_x == s_x and k_y== s_y :
        if 0 <= s_x +  move_point[m][0] < 8 and 0<= s_y +  move_point[m][1] < 8:
            s_x += move_point[m][0]
            s_y += move_point[m][1]
        else:
            k_x -= move_point[m][0]
            k_y -= move_point[m][1]


def change_chess_point(x,y):
    col = 'ABCDEFGH'
    c_x = col[x]
    c_y = str(8 - y)
    return c_x + c_y

print(change_chess_point(k_x,k_y))
print(change_chess_point(s_x,s_y))
