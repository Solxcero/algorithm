'''
(A + B) % C 는 ((A % C) + (B % C)) % C 와 같음 
=> 특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값과 이 구간 합의 나머지 연산을 한 값은 동일
=> S[i]%M 값과 S[j]%M 값이 같다면 (S[i] - S[j])%M 은 0임
=> (i, j) 쌍을 찾아서 원본리스트의 i+1 ~ j까지의 구간합이 M으로 나누어 떨어짐 확인 
'''

N, M = map(int,input().split())

A = list(map(int,input().split()))
S = [0]*N
C = [0]*M
cnt = 0

S[0] = A[0]

for i in range(1,N):
    S[i] = S[i-1]+A[i]

for i in range(N):
    remainder = S[i]%M
    if remainder == 0:
        cnt += 1
    C[remainder] += 1

for i in range(M):
    if C[i] > 1 : 
        cnt += (C[i] * (C[i]-1))//2

print(cnt)