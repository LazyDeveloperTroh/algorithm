import sys
from sys import stdin
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True

    for n in graph[v]:
        if visited[n] == False:
            dfs(graph, n, visited)
    

N = int(stdin.readline())
grid = []
for i in range(N):
    grid.append(list(stdin.readline()))

# 시계방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph_yes = [] # 적록색약인 그래프
graph_no = [] # 적록색약이 아닌 그래프

for h in range(N):
    for w in range(N):
        now_node = h*N+w
        c = grid[h][w]

        # 주변 색상비교하여 노드리스트에 저장
        node_yes = [] 
        node_no = []
        for p in range(4):
            y = h+dy[p]
            x = w+dx[p]
            next_node = y*(N)+x
            # 적록색약의 경우
            if y >= 0 and y < N and x >= 0 and x < N:
                if (c == 'R' or c == 'G') and (grid[y][x] == 'R' or grid[y][x] == 'G'):
                    node_yes.append(next_node)
                elif c == grid[y][x]:
                    node_yes.append(next_node)
            # 적록색약이 아닌 경우
            if y >= 0 and y < N and x >= 0 and x < N:
                if c == grid[y][x]:
                    node_no.append(next_node)
        graph_yes.append([now_node]+node_yes)
        graph_no.append([now_node]+node_no)

#적록색약인 경우와 아닌 경우를 각각 탐색
visited_no = [False]*N*N
visited_yes = [False]*N*N
cnt_no = 0
cnt_yes = 0

for g in graph_no:
    node = g[0]
    if visited_no[node] == False:
        dfs(graph_no, node, visited_no)
        cnt_no += 1

for g in graph_no:
    node = g[0]
    if visited_yes[node] == False:
        dfs(graph_yes, node, visited_yes)
        cnt_yes += 1
print(cnt_no, cnt_yes)

