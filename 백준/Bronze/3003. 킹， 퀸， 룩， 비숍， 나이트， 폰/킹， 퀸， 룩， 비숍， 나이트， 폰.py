# 초기 답 - 성공
a,b,c,d,e,f = map(int,input().split(' '))
print(1-a,1-b,2-c,2-d,2-e,8-f, end = ' ')

# 2번째 풀이 - 성공
import sys

userNums = list(map(int, sys.stdin.readline().strip().split(' ')))
chessNums = [1,1,2,2,2,8] # 체스 숫자를 리스트에 담고

for i in range(6):
   print(chessNums[i] - userNums[i], end = " ") # 반복해서 각각 체스 넘버에서 유저의 체스 개수만큼 빼주고 출력함
