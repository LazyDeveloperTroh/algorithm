from sys import stdin

# 입력받기
N, M, K = map(int, stdin.readline().split())

# 쓰레기좌표 초기화 
garbage = [[0] * M for _ in range(N)]
for _ in range(K):
    y, x = map(int, stdin.readline().split())
    garbage[y-1][x-1] = 1

# 방향좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방문노드
visited = [[False] * M for _ in range(N)]
# 쓰레기크기를 담는 리스트
garbage_size = []
# DFS 를 위한 스택
stack = []

for y in range(N):
    for x in range(M):
        cnt = 0
        if garbage[y][x] == 1 and visited[y][x] == False:
            stack.append([y, x])

        while stack:
            top = stack.pop()
            if visited[top[0]][top[1]] == True:
                continue
            
            cnt += 1
            visited[top[0]][top[1]] = True

            for i in range(4):
                yPos = top[0] + dy[i]
                xPos = top[1] + dx[i]
                if xPos>=0 and xPos<M and yPos>=0 and yPos<N:
                    if visited[yPos][xPos] == False and garbage[yPos][xPos] == 1:
                        stack.append([yPos,xPos])
        garbage_size.append(cnt)
print(max(garbage_size))