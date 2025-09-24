import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int,input().split())

net = [[] for _ in range(N)]
visited = [False] * (N)
found = False

for _ in range(M):
    a,b = map(int,input().split())
    net[a].append(b)
    net[b].append(a)

def dfs(v,d):
    global found
    if found:                 # (1) 함수 진입 직후 확인
        return
    if d == 5:
        found = True
        return
    
    visited[v] = True
    for i in net[v]:
        if not visited[i]:
            dfs(i,d+1)
            if found:       # (2) 자식 dfs 끝난 뒤 다시 확인
                return
    visited[v] = False

for s in range(N):
    dfs(s, 1)
    if found:
        print(1)
        break
else:
    print(0)