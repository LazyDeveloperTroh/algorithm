from collections import deque
import copy

n, m = map(int, input().split())
graph = []
result = []
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

def BFS(copy_graph):
    visit = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue = deque()
                queue.append([i, j])

                while queue:
                    v = queue.pop()
                    
                    if visit[v[0]][v[1]]:
                        continue
                    visit[v[0]][v[1]] = True

                    for k in range(4):
                        ny = v[0]+dy[k]
                        nx = v[1]+dx[k]

                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue

                        if not visit[ny][nx] and copy_graph[ny][nx] == 0:
                            copy_graph[ny][nx] = 2
                            queue.append([ny, nx])

def make_wall(count):
    if count == 3:
        copy_graph = copy.deepcopy(graph)
        BFS(copy_graph)
        cnt = 0
        for i in range(n):
            cnt += copy_graph[i].count(0)
        result.append(cnt)
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    make_wall(count+1)
                    graph[i][j] = 0
make_wall(0)
print(max(result))