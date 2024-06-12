# 실버 IV
'''
K 번째 사람이 빠지면 K + 1 번째 사람부터 다시 순서 세기
메모리  34000KB
시간    68ms
'''
import sys
from collections import deque
import time

# 1
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

# 2 
# input= sys.stdin.readline
# N, K = map(int,input().split())
# circle = list(range(1,N+1))
# s = time.time()
# i = 0 

# print('<',end='')
# while True : 
#     i = (i+K-1)%len(circle)
#     print(circle[i],end='')
#     del circle[i]
#     if len(circle) == 0 :
#         break
#     print(', ',end='')
# print('>')
# # e  = time.time()
# # print('\n',e-s)