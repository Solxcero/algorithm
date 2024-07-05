import sys

input = sys.stdin.readline

N, K  = map(int,input().split())

dp = [0] * (K+1)
for i in range(N):

    w, v = map(int,input().split())
    for j in range(K,w-1,-1):
        print(i,j)
        dp[j] = max(dp[j], dp[j-w]+v)
        print(dp)
print(dp[K])
    
    

'''
4 7
6 13
4 8
3 6
5 12

> 14
'''

# import sys

# input = sys.stdin.readline

# N, K = map(int, input().split())

# items = []
# for _ in range(N):
#     w, v = map(int, input().split())
#     items.append((w, v))

# # DP 테이블 초기화
# dp = [[0] * (K + 1) for _ in range(N + 1)]

# # DP 테이블 갱신
# for i in range(1, N + 1):
#     weight, value = items[i-1]
#     for w in range(K + 1):
#         if w >= weight:
#             dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight] + value)
#         else:
#             dp[i][w] = dp[i-1][w]

# # 최대 가치 출력
# print(dp[N][K])
