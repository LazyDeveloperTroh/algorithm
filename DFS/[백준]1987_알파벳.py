from sys import stdin

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def dfs(y, x, cnt, visited):
    global max 

    # 최대방문수 비교
    if max < cnt:
        max = cnt

    for i in range(4):
        yPos = y + dy[i]
        xPos = x + dx[i]
        if xPos>=0 and xPos<C and yPos>=0 and yPos<R:
            # 방문한 알파벳이 아니면 dfs 실행
            if visited[board[yPos][xPos]] == False:
                cp = list(visited)
                cp[board[yPos][xPos]] = True
                dfs(yPos, xPos, cnt+1, cp)

R, C = map(int, stdin.readline().split())
board = []
for _ in range(R):
    board.append(list(map(lambda a: ord(a) - 65, stdin.readline())))

history = [False] * 26
history[board[0][0]] = True
max = 1

dfs(0, 0, 1, history)
print(max)
