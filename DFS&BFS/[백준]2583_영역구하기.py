from collections import deque

# m 세로, n 가로, k 직사각형수
m, n, k = map(int, input().split())

# 직사각형을 1로 채움, 문제의 y축 좌표계는 일반적인 경우와 다르지만 대칭이기 때문에 무시하고 진행
graph = [[0] * n for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

visit = [[False] * n for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = []
for i in range(m):
    for j in range(n):
        # 빈칸을 만났을 때 BFS 실행하여 면적을 저장
        if graph[i][j] == 0:
            size = 0
            q = deque()
            q.append([i, j])

            while q:
                v = q.popleft()
                if visit[v[0]][v[1]]:
                    continue

                visit[v[0]][v[1]] = True
                size += 1

                for k in range(4):
                    ny = v[0] + dy[k]
                    nx = v[1] + dx[k]

                    if ny < 0 or ny >= m or nx < 0 or nx >= n:
                        continue

                    if graph[ny][nx] == 0 and not visit[ny][nx]:
                        q.append([ny, nx])
            if size != 0:
                result.append(size)

print(len(result))
result.sort()
for r in result:
    print(r, end=" ")