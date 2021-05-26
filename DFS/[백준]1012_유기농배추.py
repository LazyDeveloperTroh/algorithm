from sys import stdin

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(stdin.readline())
while T > 0:
    M, N, K = map(int, stdin.readline().split())

    ground = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        ground[y][x] = 1

    stack = []
    visited = [[False] * M for _ in range(N)]
    
    result = 0
    for y in range(N):
        for x in range(M):
            if ground[y][x] == 1 and visited[y][x] == False:
                stack.append([y, x])
                result += 1

            while stack:
                top = stack.pop()
                visited[top[0]][top[1]] = True

                for i in range(4):
                    yPos = top[0]+dy[i]
                    xPos = top[1]+dx[i]
                    if yPos >= 0 and yPos < N and xPos >= 0 and xPos < M:
                        if ground[yPos][xPos] == 1 and visited[yPos][xPos] == False:
                            stack.append([yPos, xPos])
    print(result)
    T -= 1


