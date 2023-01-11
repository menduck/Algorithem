'''
# 문제풀이
- 오른쪽 기준으로 정렬해서 출력하기
- rjust()이용해서 푸는 방법
- for문을 활용해 공백을 채워주는 방법
'''
# rjust()이용해서 푸는 방법
import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
  print((i*'*').rjust(N))

# for문 활용해 공백을 채워주는 방법
# import sys
# N = int(sys.stdin.readline())
# for i in range(1,N+1):
#   print((' '*(N-i))+(i*'*'))

'''
# 새롭게 배운 점
- 왼쪽 정렬
> str.ljust(전체 자리 수) 

```py
print('5'.ljust(5)) # 5
```

- 오른쪽 정렬
> str.rjust(전체 자리 수)

```py
print('5'.rjust(5)) #     5
```


- 공백을 0으로 채우는 zFill
> str.zFill(전체 자리 수)

```py
print('5'.zFill(5)) # 00005
```

'''