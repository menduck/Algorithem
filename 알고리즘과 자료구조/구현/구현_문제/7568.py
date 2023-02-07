# 7568 덩치

'''
# 문제 풀이
- 덩치가 크다의 조건
  1. 몸무게가 더 많이 나가고 
  <and>
  2. 키가 더 커야 한다.

- 두 가지 조건을 동시에 만족 시키는 사람들의 수를 계산하고 +1를 해준다.
'''
# solution - 성공
import sys
n = int(sys.stdin.readline().strip())
data =[list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)] 


# filter를 통해 2가지 조건을 충족 시키는 리스트를 추출하고 리스트의 개수를 저장한다.
for i in data:
    ranking = len(list(filter(lambda x: x[0]>i[0] and x[1]>i[1],data))) +1
    print(ranking)

'''
## 새롭게 알게된 점
- filter(function, iterable)

- lambda를 활용하여 filter에 사용하기

```py
numbers = [1,2,3,4,5]
over_five = filter(lambda number: number <5, numbers)
# filter는 iterator로 반환한다.
print(over_five) # <filter object at 0x0000025F98A0B370>

over_five_list = list(over_five)
# 그래서 list 형태로 감싸주고 출력해야한다.
print(over_five_list) # [1, 2, 3, 4]
```

- lambda를 활용해 이중 리스트에 filter 사용하기

```py
users = [['minsu', 20],['taewoo', 30],['ari', 13]]

# 10대 유저 리스트 추출하기
teenage_user = list(filter(lambda user: 20>user[1]>=10, users))
print(teenage_user) # [['ari', 13]]

# 10대 유저의 총 인원
number_teenage_user = len(teenage_user)
print(number_teenage_user) # 1
```

'''
