def solution(hp):
    result = 0
    while hp > 0:
        if hp >=5:
            result += hp//5
            hp = hp%5
        elif hp >= 3:
            result += hp//3
            hp = hp%3
        else:
            result += hp
            break
    return result