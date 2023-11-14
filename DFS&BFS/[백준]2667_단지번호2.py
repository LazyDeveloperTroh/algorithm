import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
n = int(input().strip())

# 그래프 초기화
graph=[]
for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))

# dfs 탐색, 집의 수(cnt) 전역 변수로 관리
visited = [[False]*n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
cnt = 0

def dfs(x, y):
    # 이미 방문한 노드 제외
    if visited[y][x]:
        return
    
    # 방문처리
    visited[y][x] = True
    global cnt
    cnt += 1

    # 4방향 탐색 후 이동
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[ny][nx] == 1 and visited[ny][nx] == False:
            dfs(nx, ny)

answer = []
for y in range(n):
    for x in range(n):
        if graph[y][x] == 1 and not visited[y][x]:
            cnt = 0
            dfs(x, y)
            answer.append(cnt)

print(len(answer))
answer.sort()
for cnt in answer:
    print(cnt)