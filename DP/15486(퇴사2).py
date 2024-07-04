import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
max_income = 0 
# days = []

for i in range(N):
    t, p = map(int,input().split())
    if i + t <= N:
        # days.append((t, p))
        dp[i+t] = max(dp[i+t], dp[i]+p)
    dp[i + 1] = max(dp[i + 1], dp[i]) # 현재 날까지의 최대 수익 다음날에 적용
    print(dp)

print(dp[N])




'''
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

> 55

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

> 20

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50

> 90
'''