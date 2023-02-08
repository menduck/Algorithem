# 1251 단어 나누기
# 문제 풀이
'''
- 주어진 입력값을 3개의 단어로 나눈다.
- 3개의 단어를 각각 뒤집고[::-1] 다시 합치어 빈 리스트에 추가한다.
- 리스트를 정렬하고 젤 첫번째 요소를 출력한다.
'''

# solution
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

# 세부 정리 / 하나의 단어를 세 개의 단어로 나누기

# 각각의 단어는 적어도 1이상인 단어임으로 i는 1부터 시작
for i in range(1,len(word)):
    for j in range(i+1,len(word)):
        first_word = word[:i][::-1]
        second_word = word[i:j][::-1]
        third_word = word[j:][::-1]
        print(first_word,second_word,third_word)
'''
word = mobitel 일때 출력값은
m o letib
// i = 1, j = 2 
// first_word = word[:1][::-1] = m
// second_word = word[1:2][::-1] = o
// third_word = word[2:][::-1] = letib

m bo leti
m ibo let
m tibo le
m etibo l
om b leti
om ib let
om tib le
om etib l
bom i let
bom ti le
bom eti l
ibom t le
ibom et l
tibom e l
'''