import sys 
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())

def bfs(N, K):
    # 초기 설정
    dq = deque([(N, 0)])  # (현재 위치, 시간)
    visited = [False] * 100001 # 방문 체크 배열
    visited[N] = True  # 시작 위치 방문 처리

    # BFS 루프
    while dq:
        now_pos, now_time = dq.popleft()
        print(f'현재 위치 :{now_pos} / 현재 시간 : {now_time}')
        
        # 동생 위치에 도달한 경우
        if now_pos == K:
            return now_time
        
        # 다음 위치로 이동 가능한 경우를 탐색
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            print(f'어디로? : {next_pos}')
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                print(f'방문했음 : {visited[N:K+1]}')
                dq.append((next_pos, now_time + 1)) # 이동한 결과 저장
                print(f'방문 필요: {dq}')
            else:
                print('경계 벗어났다!')
        print()

print(bfs(N,K))