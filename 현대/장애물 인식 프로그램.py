import sys
from collections import deque
input = sys.stdin.readline

arr = []
n = int(input().strip())
for _ in range(n):
    arr.append(list(map(int, list(input().strip()))))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = []
for i in range(n):
    for j in range(n):
        # 장애물을 만나면 bfs로 탐색
        if arr[i][j] == 1:
            cnt = 0
            q = deque()
            q.append([j, i])

            while q:
                x, y = q.popleft()
                
                # 해당위치 방문처리, 장애물 수 증가
                # 0인지 한번 더 체크하는 이유? 큐에서 뽑을 때 방문처리를 하기때문에
                # 방문 처리 이전에 같은 노드를 탐색한다면 큐에 중복으로 들어갈수있기 때문
                if arr[y][x] == 0:
                    continue
                arr[y][x] = 0
                cnt += 1

                # 4방향 검사
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if arr[ny][nx] == 1:
                        q.append([nx, ny])
            result.append(cnt)
result.sort()
print(len(result))
for cnt in result:
    print(cnt)