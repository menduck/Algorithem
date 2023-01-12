import sys
n = int(sys.stdin.readline())
sum  = 0
for i in range(1,n+1) : # 1부터 n까지 순회하려면, range의 두번째 인자는 끝 숫자로 포함하지 않으므로 n+1로 지정해야 한다.
  sum += i # i를 sum에 누적해서 더해준다.
print(sum)