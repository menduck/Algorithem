'''
문제풀이
- 자연수를 문자열로 바꾸고 map을 통해 하나씩 정수형으로 바꾸고 list로 만든다.
- 리스트의 요소 하나씩 for문으로 순회하면서 누적합한다.
- 아니면 sum()으로 다 더해버린다.
'''
N = list(map(int,str(input())))
print(sum(N))