import sys
word = sys.stdin.readline().strip()
new_word_list = []
for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        first_word = word[:i][::-1]
        second_word = word[i:j][::-1]
        third_word = word[j:][::-1]
        new_word_list.append(first_word+second_word+third_word)
sort_new_word=sorted(new_word_list)
print(sort_new_word[0])