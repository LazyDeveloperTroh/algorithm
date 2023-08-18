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
                        print(y, x, [ny, nx])
                        q.append([nx, ny])
            result.append(cnt)
result.sort()
print(len(result))
for cnt in result:
    print(cnt)