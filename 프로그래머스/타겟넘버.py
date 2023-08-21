from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    q = deque()
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            
            # 처음 방문한 노드, 이전 노드까지 이동한 거리 +1
            if maps[ny][nx] == 1:
                q.append([nx, ny])
                maps[ny][nx] = maps[y][x]+1
            # 이미 방문한 적이 있는 노드인 경우, 더 빠른 경로인 경우만 큐에 추가
            elif maps[ny][nx] != 0 and maps[ny][nx] != 1:
                if maps[y][x]+1 < maps[ny][nx]:
                    q.append([nx, ny])
                    maps[ny][nx] = min(maps[ny][nx], maps[y][x]+1)

    # 목적지까지 이동한 횟수
    answer = maps[n-1][m-1]

    # 목적지까지 이동 가능한 경우 이동횟수가 최소 2이상일 수 있음,
    if answer == 1:
        answer = -1
    return answer

print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,1],
                [0,0,0,0,1]]	))