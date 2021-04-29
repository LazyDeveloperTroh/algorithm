# . 필드, # 울타리, o 양, v 늑대
# 울타리로 영역을 나누고 양과 늑대의 수를 비교하여 결과값 도출

from sys import stdin 

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

R, C = map(int, stdin.readline().split())
# 울타리 초기화
fence = []
for i in range(R):
    fence.append(list(stdin.readline()))

visited = [[False]*C for _ in range(R)]

stack = []
total_sheep = 0
total_wolf = 0
for y in range(R):
    for x in range(C):
        if visited[y][x] == False and fence[y][x] != '#': 
            sheep= 0
            wolf = 0

            stack.append([y, x])
            while stack :
                top = stack.pop()
                # 방문한적이 있는 노드라면 스킵
                if visited[top[0]][top[1]] == True:  
                    continue

                if fence[top[0]][top[1]] == 'o':
                    sheep += 1
                if fence[top[0]][top[1]] == 'v':
                    wolf += 1
                visited[top[0]][top[1]] = True

                for i in range(4):
                    posY = top[0]+dy[i]
                    posX = top[1]+dx[i]
                    # 펜스내부
                    if posY >= 0 and posY < R and posX >= 0 and posX < C and visited[posY][posX] == False :
                        c = fence[posY][posX]
                        if c == 'o' or c == 'v' or c == '.':
                            stack.append([posY,posX])
            #print(y, x, sheep, wolf)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
print(total_sheep, total_wolf)