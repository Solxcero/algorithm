import sys

input = sys.stdin.readline

N = int(input())
blocks = str(input().strip())

jump_order = {'B':'O','O':'J','J':'B'}

max_energy = 999*999 + 1
# 소요된 에너지를 저장 -> 최솟값 업데이트를 위해 최댓값으로 저장
dp = [max_energy] * N
dp[0] = 0  # 처음 위치에서 에너지 0 -> 즉, dp[i] 는 i칸에 가기 위한 에너지의 최솟값

for i in range(N):
    # if dp[i] == max_energy:   # 조건문 오버헤드 발생 가능성
    #     continue  
    for j in range(i+1,N):
        if blocks[j] == jump_order[blocks[i]]:
            dp[j] = min(dp[j],(j-i)*(j-i)+dp[i])
            # print(dp)

print(dp[-1] if dp[-1] != max_energy else -1)


'''
9
BOJBOJBOJ

> 8


8
BJJOOOBB

> -1

13
BJBBJOOOJJJJB

> 50

2
BO

> 1

15
BJBOJOJOOJOBOOO

> 52
'''

# import sys

# # 재귀 한도를 10000으로 설정
# sys.setrecursionlimit(10000)

# input = sys.stdin.readline

# N = int(input())
# blocks = str(input().strip())

# jump_order = {'B': 'O', 'O': 'J', 'J': 'B'}
# max_energy = 1000 * 1000 + 1

# # 메모이제이션을 위한 리스트 초기화
# dp = [max_energy] * N

# def min_energy(i):
#     if i == N - 1:
#         return 0
#     if dp[i] != max_energy:
#         return dp[i]

#     for j in range(i + 1, N):
#         if blocks[j] == jump_order[blocks[i]]:
#             dp[i] = min(dp[i], (j - i) * (j - i) + min_energy(j))

#     return dp[i]

# result = min_energy(0)
# print(result if result != max_energy else -1)