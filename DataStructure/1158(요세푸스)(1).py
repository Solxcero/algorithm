# 실버 IV
'''
K 번째 사람이 빠지면 K + 1 번째 사람부터 다시 순서 세기
메모리  34000KB
시간    68ms
'''
import sys
from collections import deque
import time
input= sys.stdin.readline

s = time.time()
N, K = map(int,input().split())
circle = deque(range(1,N+1))

print('<',end='')
while len(circle) > 1:
    circle.rotate(-K+1)
    print(circle.popleft(),end=', ')
    # circle.popleft()
print(circle[0],end='>')
# e = time.time()
# print('\n',e-s)
