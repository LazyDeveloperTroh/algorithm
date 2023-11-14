from collections import deque
N,M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input())))
    
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]
def bfs(y, x):
    if x<0 and x>=M and y<0 and y>=N:
        return False
    
    queue = deque()
    if graph[y][x] == 1:
        queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx <0 or ny < 0 or nx >= M or ny >= N:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x]+1
                queue.append((ny, nx))
    return graph[N-1][M-1]

print(bfs(0,0))