import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
graph = []
visited = [[False] * N for i in range(N)]

for _ in range(N):
    graph.append(list(map(int, list(input().strip()))))

def BFS(i, j):
    if visited[i][j] == True or graph[i][j] == 0:
        return

    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if graph[ny][nx] == 1 and visited[ny][nx] == False:
                queue.append((ny, nx))
                visited[ny][nx] = True
                cnt += 1
    return cnt
    

cnt_list = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = BFS(i, j)
            if cnt != None:
                cnt_list.append(cnt)
cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list:
    print(cnt)