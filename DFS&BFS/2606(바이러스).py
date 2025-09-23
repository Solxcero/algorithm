import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
pair = int(input())
net = defaultdict(list)

for _ in range(pair):
    a, b = map(int,input().split())
    net[a].append(b)
    net[b].append(a)

visited = [False] * (n+1)
visited[1] = True

def dfs(v):
    print(v, net[v], visited)
    visited[v] = True

    for u in net[v]:
        if not visited[u]:
            dfs(u) 

dfs(1)
print(sum(visited)-1)


# n=int(input()) # 컴퓨터 개수
# v=int(input()) # 연결선 개수
# graph = [[] for i in range(n+1)] # 그래프 초기화
# visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
# for i in range(v): # 그래프 생성
#     a,b=map(int,input().split())
#     graph[a]+=[b] # a에 b 연결
#     graph[b]+=[a] # b에 a 연결 -> 양방향
# def dfs(v):
#     visited[v]=1
#     for nx in graph[v]:
#         if visited[nx]==0:
#             dfs(nx)
# dfs(1)
# print(sum(visited)-1)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''