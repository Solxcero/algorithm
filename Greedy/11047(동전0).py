import sys

input = sys.stdin.readline

N, K  = map(int,input().split())

coins = []

for _ in range(N):
    coins.append(int(input()))

cnt = 0
for i in range(len(coins)-1,-1,-1):
    if K == 0:
        break
        
    if coins[i] <= K:
        print(f'coin: {coins[i]}')
        cnt += K//coins[i]
        print(f'cnt : {cnt}')
        K %= coins[i]
        print(f'remain : {K}')

print(cnt)        
'''
7 4790
1
5
10
50
100
500
1000

>12

3 10
1
5
10

>1
'''