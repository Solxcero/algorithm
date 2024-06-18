import sys
input = sys.stdin.readline

N = int(input())
map_ = [list(map(int, input().rstrip())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(map_, x, y):
    stack = [(x, y)]
    map_[x][y] = 0
    count = 1

    while stack:
        x, y = stack.pop()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 경계 벗어난 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            # 집인 경우 해당 좌표 방문 처리
            if map_[nx][ny] == 1:
                stack.append((nx, ny))
                map_[nx][ny] = 0
                count += 1
            for m in map_:
                print(m)
            print()

    return count

res = []

# 단지별로 구하기 위함
for x in range(N):
    for y in range(N):
        if map_[x][y] == 1:
            res.append(dfs(map_, x, y))

res.sort()
print(len(res))
for i in res:
    print(i)


'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''