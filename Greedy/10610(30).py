import sys
input = sys.stdin.readline

N = list(map(int,input().rstrip()))

ans = 0

if 0 not in N:
    ans = -1

else:

    total_sum = sum(N)
    if total_sum%3 != 0:
        ans = -1
    else:
        N.sort(reverse=True)
        ans = int(''.join(map(str, N)))

print(ans)