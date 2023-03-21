'''
# 문제접근
- 두 변수를 swap한다.

- 자바스크립트에선 하나의 값을 임시로 저장할 변수에 저장한 후에 두 값을 바꿔주지만 파이썬에선 한 줄로 두 값을 바꿔치기 할 수 있다.

```js
a = 3;
b = 5;
temp = a;
a = b;
b = temp;
console.log(a,b) // 5 3
```

```py
a = 3
b = 5
a, b = b, a
print(a,b) # 5 3
'''
def solution(my_string, num1, num2):
    my_list = list(my_string)
    my_list[num1],my_list[num2] = my_list[num2],my_list[num1]
    
    return ''.join(my_list)
