import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 그래프 초기화
n, m = map(int, input().strip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))

# bfs 실행
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def bfs(x, y):
    #if visited[y][x]:
    #    return
    
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()

        # 4방향을 돌면서 이동가능한 곳을 queue에 저장, 이동할 때 이동횟수 계산
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] != 0:
                # 다음 이동장소의 값이 1이 아니라는 건 이미 다른 경로를 통해 방문한 적이 있다는 의미이다.
                # 이미 방문한 이력이 있는 경우 최소값만 갱신한다.
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append([nx, ny])
                else:
                    graph[ny][nx] = min(graph[ny][nx], graph[y][x] + 1)
bfs(0, 0)  
print(graph[n-1][m-1])
