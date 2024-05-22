'''
N : 재료의 개수
M : 갑옷을 만드는 데 필요한 수 

6
9
2 7 4 1 5 3
'''

N = int(input())
M = int(input())

A = list(map(int,input().split()))
A.sort()

i = 0
j = N-1
cnt = 0

while i < j:
    if A[i] + A[j] > M :
        j -= 1
    elif A[i] + A[j] == M :
        cnt += 1
        i += 1
        j -= 1
    elif A[i] + A[j] < M :
        i += 1

print(cnt)