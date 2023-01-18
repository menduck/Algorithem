import sys
numbers = list(map(int,sys.stdin.readline().strip().split()))

while True:
  for i in range(0,len(numbers)-1):
    if numbers[i] > numbers [i+1]:
      numbers[i], numbers [i+1] =  numbers [i+1],  numbers [i]
      print(*numbers)
  if numbers == [1,2,3,4,5]:
    break