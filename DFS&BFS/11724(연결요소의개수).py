import sys 

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    stack = [v]
    print(f'방문 : {stack}')
    while stack:
        node = stack.pop()
        print(f'방문 노드 : {node}')
        if not visited[node]:
            visited[node] = True
            print(f'방문함 : {visited}')
            for n in graph[node]:
                if not visited[n]:
                    stack.append(n)
                    print(f'stack 추가: {stack}')

for i in range(1, N+1):
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
        print(f'연결요소 추가: {cnt}\n')

print(cnt)


'''
6 5
1 2
2 5
5 1
3 4
4 6
'''