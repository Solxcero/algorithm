import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# DP 테이블 초기화
dp = [0] * (K + 1)

# 각 물건을 순차적으로 고려
for i in range(N):
    w, v = map(int, input().split())
    # 임시 배열 생성
    new_dp = dp[:]
    for j in range(w, K + 1):
        new_dp[j] = max(dp[j], dp[j - w] + v)
    dp = new_dp

# 최대 가치 출력
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

# N, K  = map(int,input().split())

# dp = [0] * (K+1)
# for i in range(N):

#     w, v = map(int,input().split())
#     for j in range(K,w-1,-1):
#         print(i,j)
#         dp[j] = max(dp[j], dp[j-w]+v)
#         print(dp)
# print(dp[K])

