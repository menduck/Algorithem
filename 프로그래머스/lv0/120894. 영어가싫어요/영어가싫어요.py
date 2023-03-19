'''
# 문제 접근
- 영어로 표기된 numbers를 숫자로 표기하는 문제

'''
# solution1 - startswith 활용
def solution(numbers):
    words = { "zero" : 0, "one" : 1, "two" : 2, "three": 3, "four": 4, "five" : 5, "six" : 6, "seven": 7, "eight": 8, "nine": 9 }
    result = ''
    i = 0
    while i < len(numbers):
        for w in words:
            if numbers[i:].startswith(w):
                result += str(words[w])
                i += len(w)
                break
    return int(result)

# solution2 - replace 활용
def solution(numbers):
    words =  ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i,word in enumerate(words):
        numbers = numbers.replace(word,str(i))
    return int(numbers)

'''
# 새롭게 배운점

> str.startswith('시작되는 문자열')

- str 문자열이 특정 문자열로 시작하는지 확인한다. 

'''