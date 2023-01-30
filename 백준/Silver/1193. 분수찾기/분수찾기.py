import sys
N = int(sys.stdin.readline().strip())
case = 0
end = 0
while N > end:
    case += 1
    end += case

index_num = end - N +1

if case % 2 == 0:
    print(f'{case-index_num+1}/{index_num}')
else:
    print(f'{index_num}/{case-index_num+1}')