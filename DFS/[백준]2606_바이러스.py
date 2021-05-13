from sys import stdin

# 입력 초기화
c = int(stdin.readline())
pair = int(stdin.readline())

link = [[] for i in range(c)]
for _ in range(pair):
    L1, L2 = list(map(int, stdin.readline().split()))
    link[L1-1].append(L2-1)
    link[L2-1].append(L1-1)

# 방문체크
visited = [False] * c

# 깊이탐색
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

# 결과
dfs(link, 0, visited)

cnt = 0 
for v in visited:
    if v == True:
        cnt += 1
print(cnt-1)