import sys
input = sys.stdin.readline

N, S, M = map(int,input().split())
volumes = list(map(int,input().split()))


def guitarist(N,S,M,volumes):
    dp = [[False]*(M+1) for _ in range(N+1)]

    # 시작 볼륨 표시 
    dp[0][S] = True

    for i in range(1,N+1):
        for v in range(M+1):
            if dp[i-1][v]:
                if v + volumes[i-1] <= M:
                    dp[i][v + volumes[i-1]] = True
                if v - volumes[i-1] >= 0:
                    dp[i][v - volumes[i-1]] = True
                    
                    
    for d in dp:
        print(d)
        
    for v in range(M, -1, -1):
        if dp[N][v]:
            return v
    
    return -1

print(guitarist(N,S,M,volumes))
    

'''
3 5 10
5 3 7
> 10


4 8 20
15 2 9 10
> -1

14 40 243
74 39 127 95 63 140 99 96 154 18 137 162 14 88
> 238

'''

# def guitarist(N, S, M, volumes):
#     memo = {}

#     def dfs(index, now):
#         if index == N:
#             return now
        
#         if (index, now) in memo:
#             return memo[(index, now)]
        
#         max_vol = -1
#         if now + volumes[index] <= M:
#             max_vol = max(max_vol, dfs(index + 1, now + volumes[index]))
#         if now - volumes[index] >= 0:
#             max_vol = max(max_vol, dfs(index + 1, now - volumes[index]))
        
#         memo[(index, now)] = max_vol
#         return max_vol

#     result = dfs(0, S)
#     return result if result != -1 else -1

# print(guitarist(volumes, S, M)) 
