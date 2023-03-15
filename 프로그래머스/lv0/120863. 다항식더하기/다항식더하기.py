def solution(polynomial):
    group = polynomial.split(' + ') # ['3x', '7', 'x']
    
    x_sum = 0
    num_sum = 0
    for g in group:
        if g == 'x':
            x_sum += 1
        elif 'x' in g:
            x_sum += int(g.split('x')[0])
        else:
            num_sum += int(g)

    if x_sum > 1:
        if num_sum:
            return f'{x_sum}x + {num_sum}'
        else:
            return f'{x_sum}x'

    elif x_sum == 1:
        if num_sum:
            return f'x + {num_sum}'
        else:
            return 'x'
    else:
        return f'{num_sum}'

print(solution("x + 8"))
print(solution("15 + 8"))