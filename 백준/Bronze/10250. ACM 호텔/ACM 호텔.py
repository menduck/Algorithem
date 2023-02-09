import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
  h,w,n = map(int, sys.stdin.readline().strip().split())
  buliding, unit = [str(h), str((n//h))] if n%h == 0 else[ str(n%h),str((n//h)+1)]

  print(buliding,unit.zfill(2),sep='')