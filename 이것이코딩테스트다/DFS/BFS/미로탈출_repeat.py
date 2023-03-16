from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, list(input()))))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(y, x):
    queue = deque()
    if graph[y][x] == 1:
        queue.append([y, x])

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if ny<0 or ny >= N or nx <0 or nx >= M:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x]+1
                queue.append([ny,nx])
    return graph[N-1][M-1]
print(bfs(0,0))

