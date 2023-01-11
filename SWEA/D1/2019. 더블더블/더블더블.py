'''
문제 풀이

- 0부터 주어진 횟수만큼 for문을 순회하면서 
- 2의 (0부터 주어진 횟수번째)거듭제곱을 list에 더한다.

'''
count = int(input())

result = []
for i in range(count+1) :
  result.append(2**i)
print(*result)