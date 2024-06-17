import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
print(arr)

# 각 노드의 인접 리스트를 오름차순으로 정렬
for neighbours in arr:
    neighbours.sort()
print(arr)

# DFS Stack
def dfs(arr, start):
    visited = [False] * (N + 1)
    stack = [start]

    while stack:
        v = stack.pop()
        if not visited[v]:
            print(v, end=' ')
            visited[v] = True
            stack.extend(reversed(arr[v]))
    print()

# BFS
def bfs(arr, start):
    visited = [False] * (N + 1)
    dq = deque([start])
    visited[start] = True

    while dq:
        v = dq.popleft()
        print(v, end=' ')
        
        for neighbor in arr[v]:
            if not visited[neighbor]:
                dq.append(neighbor)
                visited[neighbor] = True
    print()

dfs(arr, V)
bfs(arr, V)


'''

4 5 1
1 2
1 3
1 4
2 4
3 4


5 5 3
5 4
5 2
1 2
3 4
3 1
'''