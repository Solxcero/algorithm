import sys
input = sys.stdin.readline

N, M = map(int,input().split())

cnt = 0

if N == 1: # 세로길이가 1 일 때 (이동 못함)
    cnt =  1
    
elif N == 2: # 세로길이가 2일 때  ( 가로 길이가 5보다 크면 무조건 4가지 이동 방법을 다 써야 하지만 세로길이의 제약으로 불가 )
    cnt =  min(4, (M + 1) // 2)

elif N >= 3 and M < 7: # 가로 길이가 7보다 작을 때 (4번 이동시 오른쪽으로 6번 이동)
    cnt =  min(4, M)

elif N >= 3 and M >= 7:
    cnt =  M - 2

print(cnt)




    