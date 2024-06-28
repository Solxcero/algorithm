import sys

input = sys.stdin.readline

N = int(input())

ropes = []

for _ in range(N):
    ropes.append(int(input()))
    
ropes.sort(reverse=True)
max_weight = 0

# k개의 로프를 사용할 때 들어올릴 수 있는 최대 중량 계산
for i in range(N):
    weight = ropes[i] * (i + 1)
    if weight > max_weight:
        max_weight = weight

print(max_weight)

'''
9
5
2
1
1
1
1
1
1
1

> 9


5
5
4
2
2
2

>10
'''