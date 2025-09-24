import sys
sys.setrecursionlimit(10000)

N = int(input())

def is_prime(v: int) -> bool:
    if v < 2:
        return False
    if v % 2 == 0:
        return v == 2
    i = 3
    # √v까지만
    limit = int(v**0.5)
    while i <= limit:
        if v % i == 0:
            return False
        i += 2
    return True

def dfs(v: int, depth: int): # N 자리수 확인을 문자열이 아니라 매개변수로 하다니 나이스
    if depth == N:
        print(v)
        return
    for d in (1, 3, 7, 9):  # 말단 후보 축소
        nv = v * 10 + d
        if is_prime(nv):
            dfs(nv, depth + 1)

# 시작 숫자는 한 자리 소수만
for start in (2, 3, 5, 7):
    if N >= 1:
        if N == 1:
            print(start)
        else:
            dfs(start, 1)
