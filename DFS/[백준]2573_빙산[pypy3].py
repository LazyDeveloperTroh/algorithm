from sys import stdin
from copy import deepcopy

# 입력 초기화
N, M = map(int, stdin.readline().split())
sea = []
for _ in range(N):
    sea.append(list(map(int, stdin.readline().split())))

# 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def get_unmelt_cnt():
    cnt = 0
    for y in range(1, N-1):
        for x in range(1, M-1):
            if sea[y][x] != 0:
                cnt+=1
    return cnt

years = 0
while get_unmelt_cnt() != 0:    
    copy_sea = deepcopy(sea)

    visited = [[False] * M for _ in range(N)]# 방문비교
    stack = []
    dfs = False # 탐색이력

    for y in range(1, N-1):
        for x in range(1, M-1):
            if sea[y][x] != 0:
                # 빙산의 일부 발견하면 연결된 빙산을 DFS 탐색
                if sea[y][x] != 0 and visited[y][x] == False:
                    # 2번이상 dfs를 실행했다면 빙산은 분리된 것으로 판단하고 종료
                    if dfs == True:
                        print(years)
                        quit()

                    stack.append([y,x])
                    while stack:
                        top = stack.pop()
                        if visited[top[0]][top[1]] == True:
                            continue

                        visited[top[0]][top[1]] = True
                        for i in range(4):
                            yPos = top[0]+dy[i]
                            xPos = top[1]+dx[i]
                            
                            # 각 방향에 빙산이 있으면 스택에 추가하고
                            # 각 방향에 바다가 있으면 COPY와 비교하여 처음부터 바다였는지 비교하고 녹임
                            if sea[yPos][xPos] > 0 and visited[yPos][xPos] == False:
                                stack.append([yPos, xPos])    
                            elif sea[top[0]][top[1]] > 0 and sea[yPos][xPos] == 0 and copy_sea[yPos][xPos] == 0:
                                sea[top[0]][top[1]] -= 1
                    dfs = True
    years += 1
print(0)