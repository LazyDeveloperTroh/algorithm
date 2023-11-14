import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())

graph = []
result = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visit = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

global area
area = 1
def DFS(y, x):
    visit[y][x] = True

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if graph[ny][nx] == 1 and not visit[ny][nx]:
            DFS(ny, nx)
            global area
            area += 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visit[i][j]:
            DFS(i, j)
            result.append(area)
            area = 1

print(len(result))
if len(result) == 0:
    print(0)
else:
    print(max(result))