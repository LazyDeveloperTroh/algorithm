import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

m, n = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

global result
result = 0

def DFS(x, y):
    # 마지막 위치로 이동했다면 결과값 증가
    if x+1 == n and y+1 == m:
        global result
        result += 1
        return 
    
    h = graph[y][x]
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]

        # 배열 범위 확인
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 이동방향의 높이
        nh = graph[ny][nx]
        if nh < h :
            DFS(nx, ny)

DFS(0, 0)
print(result)


