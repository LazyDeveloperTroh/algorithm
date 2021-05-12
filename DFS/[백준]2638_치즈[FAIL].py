from sys import stdin

# 변수 초기화
N, M = map(int, stdin.readline().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, stdin.readline().split())))

# 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 외부공기를 2로 초기화
def init_air(arr) :
    air_stack = []
    air_visited = [[False] * M for _ in range(N)]
    execute = False
    for y in range(N):
        for x in range(M):
            if air_visited[y][x] == False and paper[y][x] == 0:
                air_stack.append([y, x])
                execute = True

            while air_stack:
                top = air_stack.pop()
                if air_visited[top[0]][top[1]] == True:
                    continue

                air_visited[top[0]][top[1]] = True
                arr[top[0]][top[1]] = 2

                for i in range(4):
                    yPos = top[0]+dy[i]
                    xPos = top[1]+dx[i]
                    if xPos>=0 and xPos<M and yPos>=0 and yPos<N:
                        if air_visited[yPos][xPos] == False and paper[yPos][xPos] == 0:
                            air_stack.append([yPos, xPos])
            if execute == True:
                break
        if execute == True:
            break

# 녹지않은 치즈 수량 취득
def get_cheese_cnt(arr) :
    cnt = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                cnt += 1
    return cnt

# 녹아야하는 치즈는 외부공기(2)로 바꿈
def melt_cheese(arr, melt_node):
    for y in range(N):
        for x in range(M):
            if [y, x] in melt_node:
                arr[y][x] = 2
                # 만약 녹는치즈가 내부공기와 닿아있는 경우 내부공기 초기화
                for i in range(4):
                    yPos = y+dy[i]
                    xPos = x+dx[i]
                    if xPos>=0 and xPos<M and yPos>=0 and yPos<N:
                        if arr[yPos][xPos] == 0:
                            init_air(paper)

# 외부공기 2로 초기화
init_air(paper)

hours = 0
while get_cheese_cnt(paper) != 0:
    melt_node = []

    for y in range(N):
        for x in range(M):
            conn_cnt = 0
            if paper[y][x] == 1:
                # 2방향 이상 외부 공기와 접촉하는 치즈는 리스트에 저장
                for i in range(4):
                    yPos = y+dy[i]
                    xPos = x+dx[i]
                    if xPos>=0 and xPos<M and yPos>=0 and yPos<N:
                        if paper[yPos][xPos] == 2:
                            conn_cnt+=1
                if conn_cnt >= 2:
                    melt_node.append([y, x])
    # 녹는 치즈가 없는경우 반복문 탈출
    if not melt_node:
        break
    melt_cheese(paper, melt_node)
    hours+=1
print(hours)