from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,list(input()))))

pos_x = [1, -1, 0, 0]
pos_y = [0, 0, 1, -1]

def dfs(y, x):
    if graph[y][x] == 0:
        return
    
    queue = deque()
    queue.append([y, x])

    while queue:
        py, px = queue.popleft()
        if graph[py][px] == 0:
            continue
        
        for i in range(4):
            dy = py+pos_y[i]
            dx = px+pos_x[i]

            if dy < 0 or dy >= N or dx < 0 or dx >= M:
                continue
            
            if graph[dy][dx] == 1:
                graph[dy][dx] = graph[py][px] + 1
                queue.append([dy, dx])
dfs(0, 0)
print(graph[N-1][M-1])
    
