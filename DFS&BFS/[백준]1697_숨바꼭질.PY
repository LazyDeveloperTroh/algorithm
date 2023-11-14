from collections import deque

N, M =map(int, input().split())

graph = [[] for i in range(100001)]

for i in range(M+1):
    if i-1 >= 0:
        graph[i].append(i-1)
    if i+1 < 100001:
        graph[i].append(i+1)
    if i*2 < 100001:
        graph[i].append(i*2)


visited = [False] * 100001
def bfs(v):
    queue = deque()
    print(graph[v])

    queue.append([0, v])
    while queue:
        cnt, v = queue.popleft()
        if v == M:
            return cnt

        visited[v] = True
        for link in graph[v]:
            if visited[link] == True:
                continue
            visited[link] = True
            queue.append([cnt+1, link])
    return -1
result = bfs(N)
print(result)