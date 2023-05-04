import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

def dfs(y, x, w, visit):
    if y < 0 or y >= N or x < 0 or x >= N:
        return False
    
    if graph[y][x] <= w or visit[y][x] == True:
        return False
    
    if graph[y][x] > w:
        visit[y][x] = True
        dfs(y+1, x, w, visit)
        dfs(y-1, x, w, visit)
        dfs(y, x+1, w, visit)
        dfs(y, x-1, w, visit)
        return True

max = 0
for w in range(0, 101):
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if dfs(i,j, w, visit):
                cnt+=1
    if cnt > max:
        max = cnt

print(max)
