import sys
word =  sys.stdin.readline().strip()

cro_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for w in cro_alphabet:
  word = word.replace(w,'+')
print(len(word))