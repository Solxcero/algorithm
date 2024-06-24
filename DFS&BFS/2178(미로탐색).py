import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())

# 미로 초기화
maze = [list(map(int, input().strip())) for _ in range(N)]

# 방향 설정 (상, 하, 좌, 우)
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # 좌, 우, 상, 하 순으로 변경

def bfs(x, y):
    # 덱 초기화 및 시작 지점 방문 처리
    dq = deque([(x, y)])
    maze[y][x] = 2  # 시작 위치를 2로 설정 (방문 여부와 경로 길이를 동시에 저장)
    for m in maze:
        print(m)
    print()

    while dq:
        current_x, current_y = dq.popleft()
        print(f'pop_x : {current_x}, pop_y : {current_y}')

        for dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy

            # 유효한 위치인지 확인하고, 방문하지 않은 길이라면
            if 0 <= next_x < M and 0 <= next_y < N and maze[next_y][next_x] == 1:
                maze[next_y][next_x] = maze[current_y][current_x] + 1
                dq.append((next_x, next_y))
                print(f'dq : {dq}')

                for m in maze:
                    print(m)
                print()
    # 도착 지점의 값 반환 (출발 지점을 2로 시작했으므로 2를 빼줌)
    return maze[N-1][M-1] - 1

# 결과 출력
print(bfs(0, 0))



# import sys 
# from collections import deque

# input = sys.stdin.readline

# N, M = map(int, input().split())

# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# maze = [[0]*M for _ in range(N)]
# visited = [[False] * M for _ in range(N)]

# for i in range(N):
#     number = input().strip()
#     for j in range(M):
#         maze[i][j] = int(number[j])

# def bfs(i, j):
#     dq = deque()
#     dq.append((i, j))
#     visited[i][j] = True

#     while dq:
#         now = dq.popleft()
#         for dx, dy in directions:
#             x, y = now[0] +  dx , now[1] + dy
#             if x >= 0 and y >= 0 and x < N and y < M:
#                 if maze[x][y] != 0 and not visited[x][y]:
#                     visited[x][y] = True

#                     ## 이 문제의 포인트 : 현재 위치의 깊이 (도달경로) 값으로 업데이트하기
#                     maze[x][y] = maze[now[0]][now[1]] + 1
#                     dq.append((x, y))
    
#     return maze[N-1][M-1]



# print(bfs(0, 0))
# for m in maze:
#     print(m)

'''
4 6
101111
101010
101011
111011
'''