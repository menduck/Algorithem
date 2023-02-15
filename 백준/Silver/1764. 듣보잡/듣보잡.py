from collections import Counter
import sys
n,m = list(map(int, sys.stdin.readline().strip().split()))

# Counter를 활용하여 이름과 중복된 개수를 딕셔너리로 반환받음.
data = Counter([sys.stdin.readline().strip() for _ in range(n+m)])

# Counter({'ohhenrie': 2, 'baesangwook': 2, 'charlie': 1, 'obama': 1, 'clinton': 1}) 

# filter를 활용하여 중복된 개수가 1이상인 명단만 추출
duplicate_data = list(filter(lambda str: data[str] > 1, data))
# ['ohhenrie', 'baesangwook']

# 사전순으로 정렬
duplicate_data.sort()

print(len(duplicate_data), *duplicate_data, sep ='\n')