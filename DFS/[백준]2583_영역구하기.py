from sys import stdin

def dfs(graph, v, visited):
    visited[v] = True

    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

# 상하좌우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

square_board = []
M, N, K = map(int, stdin.readline().split())
for y in range(M):
    square_board.append([0]*N)

for _ in range(K):
    pos = list(map(int, stdin.readline().split()))
    
    for y in range(pos[1], pos[3]):
        for x in range(pos[0], pos[2]):
            square_board[y][x]= 1

for _ in square_board:
    print(_)

graph = []
visited = [False] * M*N
for y in range(M):
    for x in range(N):
        link = []

        if square_board[y][x] == 0:
            for i in range(4):
                _dy = dy[i]
                _dx = dx[i]

                if (y+_dy) >= 0 and (y+_dy) < M and (x+_dx) >= 0 and (x+_dx) < N:
                    if square_board[y+_dy][x+_dx] == 0:
                        link_node = N*(y+_dy) + (x+_dx)
                        link.append(link_node)
        graph.append(link)
print(graph)

dfs(graph, 0, visited)