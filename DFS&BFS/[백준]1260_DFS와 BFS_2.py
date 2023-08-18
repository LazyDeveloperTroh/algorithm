from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)
for i in range(len(graph)):
    graph[i].sort()

visited = [False] * n
def dfs(v):
    if visited[v]:
        return
    visited[v] = True
    arr = graph[v]
    print(v+1, end=" ")
    for v2 in arr:
        if visited[v2]:
            continue
        dfs(v2)
dfs(v-1)

print("")
visited = [False] * n
def bfs(v):
    if visited[v]:
        return
    
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        if visited[v]:
            continue

        visited[v] = True
        print(v+1, end=" ")

        for v2 in graph[v]:
            if not visited[v2]:
                q.append(v2)
bfs(v-1)

