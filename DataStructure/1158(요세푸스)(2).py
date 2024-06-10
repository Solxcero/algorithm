# 실버 IV

### 리스트로 풀기
'''
메모리  31120KB
시간    48ms
'''
import sys
import time
input= sys.stdin.readline
N, K = map(int,input().split())
circle = list(range(1,N+1))
s = time.time()
i = 0 

print('<',end='')
while True : 
    i = (i+K-1)%len(circle)
    print(circle[i],end='')
    del circle[i]
    if len(circle) == 0 :
        break
    print(', ',end='')
print('>')
# e  = time.time()
# print('\n',e-s)
