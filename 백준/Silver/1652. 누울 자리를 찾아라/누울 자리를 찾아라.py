import sys
n = int(sys.stdin.readline().strip())
matrix = [list(sys.stdin.readline().strip()) for _ in range(n)]

def bed_count(matrix,n):
    cnt = 0
    for i in range(n):
        bed = 0
        for j in range(n):
          if matrix[i][j] == '.':
              bed += 1
          # 'X' 만났을때
          else: 
              if bed >= 2:
                  cnt += 1
                  bed = 0
              else:
                  bed = 0
        if bed >= 2:
            cnt += 1
    return cnt
print(bed_count(matrix,n),bed_count(list(zip(*matrix)),n))