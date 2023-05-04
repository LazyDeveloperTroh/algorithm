from sys import stdin

N, M = map(int, stdin.readline().split())
# 게임판 초기화
board = []
for _ in range(N):
    board.append(list(stdin.readline()))

# 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for y in range(N):
    for x in range(M):
        # 그래프가 시작점으로 복귀하는지 확인하기 위해 각 노드마다 DFS를 실행한다
        visited = [[False] * M for _ in range(N)]
        stack = []
        
        # 각 노드까지 움직인 횟수를 스택에 같이 넣어준다
        move_cnt = 0
        if visited[y][x] == False:
            stack.append([y, x, move_cnt])

        while stack:
            top = stack.pop()
            if visited[top[0]][top[1]] == True:
                continue
            
            visited[top[0]][top[1]] = True
            move = top[2]
            for i in range(4):
                yPos = top[0]+dy[i]
                xPos = top[1]+dx[i]
                if yPos >=0 and yPos < N and xPos >= 0 and xPos < M:
                    # 최소 4번 노드가 움직이고, 다음 노드가 원점과 같은 경우 원점으로 복귀한다고 판단
                    if y == yPos and x == xPos and move >= 3:
                        print("Yes")
                        exit()

                    if board[y][x] == board[yPos][xPos] and visited[yPos][xPos] == False:
                        stack.append([yPos, xPos, move+1])
print("No")