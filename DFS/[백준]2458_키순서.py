from sys import stdin

M, N  = map(int, stdin.readline().split())

dx = [0, 1, 1, 1, 0, -1, -1, -1] 
dy = [1, 1, 0, -1, -1, -1, 0, 1]

board = []
visited = [[False] * N for _ in range(M)]
for _ in range(M):
    board.append(list(map(int,stdin.readline().split())))

cnt = 0
stack = []
for y in range(M):
    for x in range(N):
        if board[y][x] == 1 and visited[y][x] == False:
            stack.append([y, x])
            cnt += 1

        while stack:
            top = stack.pop()
            visited[top[0]][top[1]] = True

            for i in range(8):
                yPos = top[0]+dy[i]
                xPos = top[1]+dx[i]
                if yPos>=0 and yPos<M and xPos>=0 and xPos<N:
                    if board[yPos][xPos] == 1 and visited[yPos][xPos] == False:
                        stack.append([yPos, xPos])
print(cnt)