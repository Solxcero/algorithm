'''
10
1 2 3 4 5 6 7 8 9 10
'''
N = int(input())
A = list(map(int,input().split()))
A.sort()

cnt = 0

for k in range(N):
    find = A[k]
    i = 0 
    j = N - 1
    while i < j :
        if A[i] + A[j] < find:
            i += 1
        elif A[i] + A[j] > find:
            j -= 1
        elif A[i] + A[j] == find:
            if i != k and j != k:
                cnt += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

print(cnt)