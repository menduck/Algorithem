import sys
word = sys.stdin.readline().strip()
not_word = 'CAMBRIDGE'
for w in word:
  if w not in not_word:
    print(w,end='')