graph1 = {1: [2, 3, 5], 2: [1, 3], 3: [1, 2, 4], 4: [3, 5], 5: [1, 4]} #무방향 그래프
graph2 = {1: [2, 3], 2: [3], 3: [4], 4: [], 5: [1, 4]}                 #방향 그래프

'''
graph1 = [[], [2, 3, 5], [1, 3], [1, 2, 4], [3, 5], [1, 4]] #무방향 그래프
graph2 = [[], [2, 3], [3], [4], [], [1, 4]]                 #방향 그래프
'''

def dfs_recursive(graph, node):
    #방문 결과를 담을 리스트와 방문 여부를 확인할 집합을 만든다.
    res = []
    visited = set()

    #깊이 우선 탐색하는 재귀함수를 만든다.
    def _dfs(u):
        # 이미 방문한 노드이면 종료한다.
        if u in visited:
            return

        #현재 노드를 방문 처리한다.
        #즉, 방문 결과 리스트와 방문 여부를 확인할 집합에 추가한다.
        visited.add(u)
        res.append(u)

        #현재 노드와 간선으로 연결된 노드들을 깊이 우선 탐색한다.
        for v in graph[u]:
            _dfs(v)

    _dfs(node)
    return res

print("무방향 그래프의 깊이 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", dfs_recursive(graph1, 1))
print("노드 2에서 시작: ", dfs_recursive(graph1, 2))
print()
print("방향 그래프의 깊이 우선 탐색")
print("========================")
print("노드 1에서 시작: ", dfs_recursive(graph2, 1))
print("노드 2에서 시작: ", dfs_recursive(graph2, 2))


def dfs(graph, node):
    #방문할 노드를 저장한 스택과 방문 여부를 확인한 집합을 만든다.
    #스택과 집합에 방문할 첫 노드를 넣는다.
    res = []
    stack = [node]
    visited = set(stack)

    #스택이 빌 때까지 반복한다.
    while stack:
        #스택에서 노드를 꺼내고 방문처리한다.
        u = stack.pop()
        res.append(u)

        #현재 노드에 연결된 다른 노드를 확인한다.
        #다른 노드가 아직 방문하지 앟는 노드이면, 스택과 집합에 넣는다.
        for v in graph[u]:
            if v not in visited:
                visited.add(v)
                stack.append(v)
    return res

print("무방향 그래프의 깊이 우선 탐색")
print("==========================")
print("노드 1에서 시작: ", dfs(graph1, 1))
print("노드 2에서 시작: ", dfs(graph1, 2))
print()
print("방향 그래프의 깊이 우선 탐색")
print("========================")
print("노드 1에서 시작: ", dfs(graph2, 1))
print("노드 2에서 시작: ", dfs(graph2, 2))
