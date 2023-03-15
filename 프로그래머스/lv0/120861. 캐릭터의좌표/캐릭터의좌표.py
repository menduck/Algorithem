# solution - 성공
def solution1(keyinput, board):
    direction = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}

    width = board[0]//2
    height = board[1]//2

    target_p = [0,0]
    for key in keyinput:
        dx = direction[key][0]
        dy = direction[key][1]

        nx = target_p[0]+dx 
        ny = target_p[1]+dy 

        if -width<=nx<=width and -height<=ny<=height:
            target_p = [nx, ny]
    return target_p

# solution - 최종 코드(코드 정리)
def solution(keyinput, board):
    direction = {'up':[0,1], 'down':[0,-1], 'left':[-1,0], 'right':[1,0]}

    width = board[0]//2
    height = board[1]//2

    target_p = [0,0]
    for key in keyinput:
        dx,dy = direction[key]

        nx, ny = target_p[0]+dx, target_p[1]+dy 

        if abs(nx)<=width and abs(ny)<=height:
            target_p = [nx, ny]
    return target_p


solution(["left", "right", "up", "right", "right"], [11, 11])