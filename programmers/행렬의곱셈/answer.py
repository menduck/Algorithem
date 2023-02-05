# 행렬의 곱셈

# 문제풀이
# - 원소 하나씩 인덱스로 접근하여 계산해줌.

# solution - 성공
def solution(arr1,arr2):
    # [[0, 0], [0, 0], [0, 0]]
    result = [[0]*len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += arr1[i][k] * arr2[k][j]
    return result

# 다른 사람 풀이 - zip
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

# - zip으로 B의 행렬을 행과 열을 바꾼다. 
# - A의 행(a,b)과 행과 열을 바꾼 B 행렬의 행(c,d)을 계산하고 리스트에 저장한다.
#   - a*c + b*d 

