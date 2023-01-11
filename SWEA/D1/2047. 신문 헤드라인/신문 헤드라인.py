'''
문제 풀이
- 언더바를 구분자로 split하여 입력받는다.
- 입력받은 리스트의 요소들을 순회하면서 대문자로 바꾼다.
- 언더바를 구분자로 하여 join하고 출력한다.
'''
headline_list = input().split('_')

upper_headline_list = []
for headline_str in headline_list :
  upper_headline_list.append(headline_str.upper())
print('_'.join(upper_headline_list))