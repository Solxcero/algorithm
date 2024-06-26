import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())

teams = min(N // 2, M)

remain = N + M - teams * 3

# 남은 인원이 K를 충족하지 못하면 팀 하나씩 해체
while remain < K:
    teams -= 1
    remain += 3

print(teams)


''' 이진탐색으로 풀기 
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

low, high = 0, min(N // 2, M)

while low <= high:
    mid = (low + high) // 2
    if N - 2 * mid + M - mid >= K:
        low = mid + 1
    else:
        high = mid - 1

print(high)


'''