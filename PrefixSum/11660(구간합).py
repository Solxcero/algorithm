import sys
input = sys.stdin.readline

N,M = map(int,input().split())

A = [[0] * (N+1)] # 2차원 원본 배열 -> 좌표(인덱스) 찾는 용도
D = [[0] * (N+1) for _ in range(N+1)] # 2차원 구간 합 배열 -> 좌표(인덱스) 찾는 용도

# 원본 배열 A 값 입력 
for i in range(1,N+1):
    A_row = [0] + [int(x) for x in input().split()] 
    A.append(A_row)


# 구간 합 배열 D 값 입력
for i in range(1,N+1):
    for j  in range(1, N+1):
        D[i][j] = D[i][j-1]  + D[i-1][j] - D[i-1][j-1] + A[i][j]

print()
print('        A               D       ')
for A_row, D_row in zip(A,D):
    print(f'{A_row}  {D_row}')
print()
# 구간 합 구하기 
for _ in range(M):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1] 
    print(f'{D[x2][y2]} - {D[x1-1][y2]} - {D[x2][y1-1]} + {D[x1-1][y1-1]} = {result}')
    print()
    
