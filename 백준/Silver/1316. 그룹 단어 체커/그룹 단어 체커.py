import sys
N = int(sys.stdin.readline().strip())

total = 0
for _ in range(N):
  word = sys.stdin.readline().strip()
  not_duplication = [word[0]]
  for i in range(len(word) -1):
    if word[i] != word[i+1]:
      not_duplication.append(word[i+1])
  if len(set(not_duplication)) == len(not_duplication) :
    total += 1
print(total) 