def solution(my_string):
    num_list = []

    for char in my_string:
        if char.isdigit():
            num_list.append(int(char))

    return sum(num_list)