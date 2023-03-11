def solution(elements):
    result = set()
    
    # 원형 수열이기 때문에
    circular_sequence = elements *2

    # 기준점을 잡고 배열의 크기 별로 부분합을 만들어 set에 추가한다.

    # 요소 시작점
    for i in range(len(circular_sequence)):
        for j in range(len(elements)):
            # print(i,i+j)
            result.add(sum(circular_sequence[i:i+j+1]))
    return len(result)



solution([7,9,1,1,4])