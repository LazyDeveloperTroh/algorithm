from sys import stdin

apartments = []
N = int(stdin.readline())
for _ in range(N):
    apartments.append(list(map(int, stdin.readline().replace("\n", ""))))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = [[False] * N for _ in range(N)]
stack = []
result = []
for y in range(N):
    for x in range(N):
        if apartments[y][x] == 1 and visited[y][x] == False:
            stack.append([y, x])
            cnt = 0
            while stack:
                top = stack.pop()
                if visited[top[0]][top[1]] == True:
                    continue

                visited[top[0]][top[1]] = True
                cnt +=1
                for i in range(4):
                    yPos = top[0]+dy[i]
                    xPos = top[1]+dx[i]
                    if xPos>=0 and xPos<N and yPos>=0 and yPos<N:
                        if apartments[yPos][xPos] == 1:
                            stack.append([yPos, xPos])
            result.append(cnt)
result.sort()

print(len(result))
for n in result:
    print(n)
