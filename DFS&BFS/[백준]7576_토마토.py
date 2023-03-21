from collections import deque

M, N = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

pos_x = [-1, 1, 0, 0]
pos_y = [0, 0, -1, 1]

def bfs(starts):
    queue = deque()
    for start in starts:
        queue.append([start[0], start[1]])
    
    # 마지막 일수를 저장함
    result = 0
    while queue:
        qy, qx = queue.popleft()
        
        for i in range(4):
            dy = qy+pos_y[i]
            dx = qx+pos_x[i]

            if dy < 0 or dy >= N or dx < 0 or dx >= M:
                continue

            if graph[dy][dx] == 0:
                graph[dy][dx] = graph[qy][qx] + 1
                queue.append([dy, dx])
                # 포인트
                result = graph[qy][qx] 
    
    # 탐색이 끝났는데도 익지않은 토마토가 있다면
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
    return result

starts=[]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            starts.append([i,j])

result = bfs(starts)
print(result)