graph = []
N, M = map(int, input().split())
for i in range(N):
    graph.append(list(input()))


def dfs(y, x):
    if y < 0 and y >= N and x < 0 and x >= M:
        return False

    if graph[y][x] == 1:
        return False
    
    graph[y][x] = 0
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)
    return True
            


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)