import sys

sentense = sys.stdin.readline().strip()

for i in range(0,len(sentense),10) :
  print(sentense[i:i+10])