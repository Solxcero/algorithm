import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int,input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1 :
            break
    
        print(f'dp[{i}][{j}] : {board[i][j]}')
        jump = board[i][j]
        if i+jump < N:
            dp[i+jump][j] += dp[i][j]
        if  j+jump < N:
            dp[i][j+jump] += dp[i][j]
            
        for d in dp:
            print(d)
        print()
        
        
print(dp[N-1][N-1])

'''
4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0

> 3


9
3 1 2 2 3 3 1 1 2
1 1 2 1 1 2 3 1 2
2 1 1 3 2 2 1 3 1
3 3 1 1 1 3 1 2 1
3 2 2 2 1 1 3 3 1
3 1 3 2 2 3 1 3 3
3 1 1 2 1 1 1 1 1
2 3 1 3 1 3 2 2 2
3 3 3 2 3 1 3 3 0

> 6


4
1 2 2 3
1 1 3 3
3 1 1 3
3 2 1 0

> 5

'''

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline


# N = int(input().strip())
# board = [list(map(int, input().split())) for _ in range(N)]
# memo = [[-1] * N for _ in range(N)]

# def count_paths(x, y):
#     # 기저 사례: 도착점에 도달한 경우
#     if x == N - 1 and y == N - 1:
#         return 1
#     # 이미 계산된 값이 있는 경우
#     if memo[x][y] != -1:
#         return memo[x][y]

#     paths = 0
#     jump = board[x][y]
#     if jump > 0:
#         if x + jump < N:
#             paths += count_paths(x + jump, y)
#         if y + jump < N:
#             paths += count_paths(x, y + jump)
    
#     # 메모이제이션
#     memo[x][y] = paths
#     return paths


# result = count_paths(0, 0)
# print(result)
    
