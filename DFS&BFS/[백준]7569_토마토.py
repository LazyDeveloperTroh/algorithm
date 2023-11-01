from collections import deque

# 가로, 세로, 높이
m, n, h = map(int, input().split())

graph = []
for i in range(h):
    graph.append([])
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

# 3차원 방향
dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 익은토마토(1), 익지않은토마토(0), 빈칸(-1)
q = deque()
none_tomato_cnt = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                q.append([k, i, j])
            elif graph[k][i][j] == 0:
                none_tomato_cnt += 1

# 처음부터 모두 익어있었다면 0 출력
if none_tomato_cnt == 0:
    print(0)
    exit()

while q:
    v = q.popleft()

    for k in range(6):
        nz = v[0] + dz[k] 
        ny = v[1] + dy[k]
        nx = v[2] + dx[k]

        if nz < 0 or nz >= h or ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if graph[nz][ny][nx] == 0:
            q.append([nz,ny,nx])
            graph[nz][ny][nx] = graph[v[0]][v[1]][v[2]] + 1

max_day = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            # 익지 않은 토마토가 있다면 -1 출력 후 종료
            if graph[k][i][j] == 0:
                print(-1)
                exit()
            else:
                max_day = max(max_day, graph[k][i][j]) 
# 1부터 시작했기 때문에 1을 빼줌
print(max_day-1)